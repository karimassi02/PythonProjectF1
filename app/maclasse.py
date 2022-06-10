import requests

if __name__ == '__main__':
    #r = requests.get('http://ergast.com/api/f1/2021/circuits.json')
    #print(r.json())


    #mtn créer une variable avec tableau qui contient toutes les années
    #concatener string + var + string
    #boucle for

    url = 'http://ergast.com/api/f1/'
    years = ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
    new_years = ['2021', '2022']

    l = []


class Circuit:
    def __init__(self):
        for year in years:
            #print(url+x+'/circuits.json')
            self.r = requests.get(url+year+'/circuits.json')
            self.data = self.r.json()
            self.data_circuit= self.data['MRData']['CircuitTable']['Circuits']
            for year in self.data_circuit:
                print(year['circuitName'], year['Location']['locality'], year['Location']['country'])


#Circuit()

class Standings:
    def __init__(self):
        for x in years:
            self.s = requests.get(url+x+'/driverStandings.json')
            self.data2 = self.s.json()
            self.data_season_end_driver_standings = self.data2['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
            for x in self.data_season_end_driver_standings:
                print(x['Driver']['givenName'], x['Driver']['familyName'])
        for x in years:
            self.t = requests.get(url+x+'/constructorStandings.json')
            self.data3 = self.t.json()
            self.data_season_end_constructor_standings = self.data3['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']
            for x in self.data_season_end_constructor_standings:
                print(x['Constructor']['name'], x['Constructor']['url'])

Standings()

class StandingsAfterGP:
    def __init__(self):
        for x in years:
            for y in range(1,23):
                self.u = requests.get(url+x+'/'+str(y)+'/driverStandings.json')
                self.data4 = self.u.json()
                if self.data4['MRData']['StandingsTable']['StandingsLists']:
                    self.data_grandprix_result = self.data4['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
                    for z in self.data_grandprix_result:
                        #print(z['Driver']['givenName'], z['Driver']['familyName'])
                        print(z['Driver']['givenName'], z['Driver']['familyName'], z['Driver']['nationality'])
                else:
                    print("N/A")
        for x in years:
            for y in range(1, 23):
                self.a = requests.get(url + x + '/' + str(y) + '/constructorStandings.json')
                self.data8 = self.a.json()
                if self.data8['MRData']['StandingsTable']['StandingsLists']:
                    self.data_constructor_after_race = self.data8['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']
                    for z in self.data_constructor_after_race:
                        # print(z['Driver']['givenName'], z['Driver']['familyName'])
                        print(z['Constructor']['name'], z['Constructor']['url'])
                else:
                    print("missing info")
#StandingsAfterGP()


class Race:
    def __init__(self):
        for x in years:
            for y in range(1,23):
                self.v = requests.get(url+x+'/'+str(y)+'/results.json')
                self.data5 = self.v.json()
                if self.data5['MRData']['RaceTable']['Races']:
                    self.data_race_result = self.data5['MRData']['RaceTable']['Races'][0]['Results']
                    for z in self.data_race_result:
                        print(z['Driver']['givenName'], z['Driver']['familyName'])
                else:
                    print("Missing info")
#Race()

class Qualifying:
    def __init__(self):
        for x in years:
            for y in range(1,23):
                self.w = requests.get(url+x+'/'+str(y)+'/qualifying.json')
                self.data6 = self.w.json()
                if self.data6['MRData']['RaceTable']['Races']:
                    self.data_qualifying = self.data6['MRData']['RaceTable']['Races'][0]['QualifyingResults']
                    for z in self.data_qualifying:
                        print(z['position'], z['Driver']['givenName'], z['Driver']['familyName'])
                else:
                    print("Missing information")
#Qualifying()


class Schedule:
    def __init__(self):
        for x in new_years:
            for y in range(1,23):
                self.z = requests.get(url+x+'/'+str(y)+'.json')
                self.data7 = self.z.json()
                if self.data7['MRData']['RaceTable']['Races']:
                    self.data_schedule = self.data7['MRData']['RaceTable']['Races']
                    for z in self.data_schedule:
                        #print (type(z))
                        if 'ThirdPractice' in z:
                            print(z['raceName'])
                            print(z['FirstPractice']['date'], ': First Practice')
                            print(z['SecondPractice']['date'], ': Second Practice')
                            print(z['ThirdPractice']['date'], ': Third Practice')
                            print(z['Qualifying']['date'], ': Qualifying')
                            print(z['date'], z['time'], ': Race')
                else:
                    #print(data7)
                    print('Missing information bro')
Schedule()



# for q in drivers:
#         b = requests.get(url+'drivers/'+q+'/driverStandings.json')
#         print(b)
#         data9 = b.json()
#         print(url+'drivers/'+q+'/driverStandings.json')
#         if data9['MRData']['StandingsTable']['StandingsList']:
#             data_specific_driver_result = data9['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
#             for z in data_specific_driver_result:
#                 print(z['position'], z['points'], z['wins'], z['Driver']['givenName'], z['Driver']['familyName'])