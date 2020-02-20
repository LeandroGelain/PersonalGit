class Trello(object):
    
    def __init__(self):
        self.key = '6950b8934d57f2f842b5e20e9df3081b'
        self.token = '83833e6c9ab00b6d7a818809644d78eb63c416a05a7b0e61c029c4e57f0ed53a'
    
    def idBoards(self):    
        self.idBoards = {
            #Time condor
            "1":"5c879757f9ec7677ec8dc306",
            "2":"5c87975b34ffb863e3562aa3",
            "3":"5c879751062e1e38a539ff28",
            "4":"5c87975f45d15517216938aa",
            "5":"5c87999941ef10370674b424",
            "6":"5c92221614b5d91db3379725",
            "7":"5c92222e1467ad7f61e8c935",
            #Time cygni
            '8':'5c5839d217bed6275c21b21e',
            '9':'5c5839501e5d3b0fe27ded1e',
            '10':'5c5837ce0e84fd5b2ed3389c',
            '11':'5c583a47a767c06173ea2b94',
            '12':'5c584165a881ef674377aae9',
            #Time Linha hunter
            '13':'5c824191de36ac70b1d13d48',
            '14':'5c8241a94ed68f0e7119cbb4',
            '15':'5c7fc82bdbfaa9778459435b',
            '16':'5c8241c980cdb87533daf1a6',
            '17':'5c8241e8e7739a3d5268abf9',
            #Time Pulverizador de barras jacto
            '18':'5c4adbcbc5904e63036157c4',
            '19':'5c4adbe24636cb179bc43a1d',
            '20':'5c4adbf61bc41f6765f8578c',
            '21':'5c4adc08abc56b51a7bbed60',
            '22':'5c5421f5993dd12a2a20d35a',
            #Time Uniport 2530
            '23':'5c6c31d173ce5308d409ef59',
            '24':'5c6c31e9e64bf81a90053a7e',
            '25':'5c6c321e0dacc41d2bf07851',
            '26':'5c6c319143dab36629e90641',
            '27':'5c6c3261f041985d43d89ac0',
            #Time Uniport 3030
            '28':'5c544907ac7603402eb900cd',
            '29':'5c544955b6e2957005ea9653',
            '30':'5c5447fbad5d3a8304ca4b6e',
            '31':'5c5449752a1dc16ff3a7f831',
            '32':'5c5449976953fa3f9611fcd0',
            #Time Iniport 5030
            '33':'5c3a913e06d11f4d953bf41b',
            '34':'5c3a9205dae4807b323464f9',
            '35':'5c3a8d94f62c481e9e9fbd80',
            '36':'5c3a92878e118e367c75e289',
            '37':'5c485b3665ee284d25f3e8ba',
            '38':'5c9222a1438324110555a610',
            '39':'5c9222b2563a6c111e4cef5e',
            #Time Veos Jacto
            '40':'5c894de00d41aa2c1422b5ce',
            '41':'5c8971078199d664d40e955c',
            #Brudden Roçadeira K430
            '42':'5cc700e67c9d080563bbad4a',
            '43':'5cc7017430db973aa43bfe72',
            '44':'5cc7003371ae5841bd86699b',
            '45':'5cc701e9690842721f7a18e5',
            '46':'5cc702697257b8877b670db6',
            #Brudden Multifuncional BMU260
            '47':'5cc704727c9d080563bcbcaa',
            '48':'5cc70496529aa56651c4b012',
            '49':'5cc704c15d28a3575ebe23d8',
            '50':'5cc704e6956a7d64bba74d8e',
            '51':'5cc70502166da08e5918e8b4'
            }
        return dict(self.idBoards)