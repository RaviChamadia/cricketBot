import requests
class cricketData:
    __api_key=""
    __url=""
    def __cricketData(self):
        res=requests.get(self.__url)
        return res.json()
    def __getMatchId(self,teamName):
        self.__url="https://cricapi.com/api/matches?apikey="+self.__api_key
        data=self.__cricketData()
        for i in data["matches"]:
            if i["matchStarted"]:
                if teamName.lower() in i["team-1"].lower() or teamName.lower() in i["team-2"]:
                    return i["unique_id"]
        return False

    def cal(self):
        self.__url="https://cricapi.com/api/matchCalendar?apikey="+self.__api_key
        data=self.__cricketData()
        info=""
        lineCount=0
        while True:
            for i in data['data']:
                info+="Name:{0}\nDate:{1}\n\n".format(i['name'],i['date'])
                if lineCount==20:
                    return info
                lineCount+=1
        

    def score(self,teamName):
        matchId=self.__getMatchId(teamName)
        if matchId:
            self.__url="https://cricapi.com/api/cricketScore?apikey="+self.__api_key+"&unique_id="+str(matchId)
            data=self.__cricketData()
            return data["score"]
        else:
            return False

    def live(self):
        self.__url="https://cricapi.com/api/matches?apikey="+self.__api_key
        data=self.__cricketData()
        info=""
        lineCount=0
        
        while True:
            
            for i in data["matches"]:
                if i["matchStarted"]:
                    date=i["date"].split("T")
                    
                    info+="{0} VS {1} Date:{2}\n\n".format(i['team-1'],i['team-2'],date[0])
                    if lineCount==20:
                        return info
                    lineCount+=1
        
                
