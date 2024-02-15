from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity

class SendMessageLayer(YowInterfaceLayer):
    def __init__(self, account_sid, auth_token, to_phone, message):
        super(SendMessageLayer, self).__init__()
        self.ackQueue = []
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.to_phone = to_phone
        self.message = message

    @ProtocolEntityCallback("success")
    def onSuccess(self, successProtocolEntity):
        self.toLower(successProtocolEntity)

    @ProtocolEntityCallback("ack")
    def onAck(self, entity):
        self.ackQueue.pop(0)
        if not self.ackQueue:
            self.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_DISCONNECT))

    def sendMessage(self):
        messageEntity = TextMessageProtocolEntity(self.message, to = self.to_phone)
        self.ackQueue.append(messageEntity.getId())
        self.toUpper(messageEntity)

if __name__ == '__main__':
    from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
    from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity

    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    to_phone = 'whatsapp_phone_number'
    message = 'Hello, WhatsApp!'

    send_message_layer = SendMessageLayer(account_sid, auth_token, to_phone, message)
    send_message_layer.sendMessage()
    send_message_layer.sendLayer()