


class getInformation:
        def __init__(self,ComponentID,ChannelID):
            self.componentid = ComponentID
            self.channelID = ChannelID
            self.IP = "127.0.0.1"
            self.Port = 8084
            self.Password = "admin"


        @property
        def link(self):
            urllink = f"http://{self.IP}:{self.Port}/rest/channel/{self.componentid}/{self.channelID}"
            return urllink
        @property
        def cid(self):
            return self.componentid

        @cid.setter
        def cid(self, value):
            self.componentid = value

        @property
        def chid(self):
            return self.channelID

        @chid.setter
        def chid(self, value):
            self.channelID = value



