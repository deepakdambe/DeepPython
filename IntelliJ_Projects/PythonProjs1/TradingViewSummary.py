
from tradingview_ta import TA_Handler, Interval

symbols200 = ["ABB","ACC","APLAPOLLO","AUBANK","ADANIENSOL","ADANIENT","ADANIGREEN","ADANIPORTS","ADANIPOWER","ATGL","AWL","ABCAPITAL","ABFRL","ALKEM",
           "AMBUJACEM","APOLLOHOSP","APOLLOTYRE","ASHOKLEY","ASIANPAINT","ASTRAL","AUROPHARMA","DMART","AXISBANK","BAJAJ_AUTO","BAJFINANCE","BAJAJFINSV",
           "BAJAJHLDNG","BALKRISIND","BANDHANBNK","BANKBARODA","BANKINDIA","BATAINDIA","BERGEPAINT","BDL","BEL","BHARATFORG","BHEL","BPCL","BHARTIARTL",
           "BIOCON","BOSCHLTD","BRITANNIA","CGPOWER","CANBK","CHOLAFIN","CIPLA","COALINDIA","COFORGE","COLPAL","CONCOR","COROMANDEL","CROMPTON","CUMMINSIND",
           "DLF","DABUR","DALBHARAT","DEEPAKNTR","DELHIVERY","DEVYANI","DIVISLAB","DIXON","LALPATHLAB","DRREDDY","EICHERMOT","ESCORTS","NYKAA","FEDERALBNK",
           "FACT","FORTIS","GAIL","GLAND","GODREJCP","GODREJPROP","GRASIM","FLUOROCHEM","GUJGASLTD","HCLTECH","HDFCAMC","HDFCBANK","HDFCLIFE","HAVELLS","HEROMOTOCO",
           "HINDALCO","HAL","HINDPETRO","HINDUNILVR","ICICIBANK","ICICIGI","ICICIPRULI","IDFCFIRSTB","ITC","INDIANB","INDHOTEL","IOC","IRCTC","IRFC","IGL",
           "INDUSTOWER","INDUSINDBK","NAUKRI","INFY","INDIGO","IPCALAB","JSWENERGY","JSWSTEEL","JINDALSTEL","JUBLFOOD","KPITTECH","KOTAKBANK","L_TFH","LTTS",
           "LICHSGFIN","LTIM","LT","LAURUSLABS","LICI","LUPIN","MRF","LODHA","M_MFIN","M_M","MANKIND","MARICO","MARUTI","MFSL","MAXHEALTH","MAZDOCK","MSUMI",
           "MPHASIS","MUTHOOTFIN","NHPC","NMDC","NTPC","NAVINFLUOR","NESTLEIND","OBEROIRLTY","ONGC","OIL","PAYTM","POLICYBZR","PIIND","PAGEIND","PATANJALI",
           "PERSISTENT","PETRONET","PIDILITIND","PEL","POLYCAB","POONAWALLA","PFC","POWERGRID","PRESTIGE","PGHH","PNB","RECLTD","RVNL","RELIANCE","SBICARD",
           "SBILIFE","SRF","MOTHERSON","SHREECEM","SHRIRAMFIN","SIEMENS","SONACOMS","SBIN","SAIL","SUNPHARMA","SUNTV","SYNGENE","TVSMOTOR","TATACHEM","TATACOMM",
           "TCS","TATACONSUM","TATAELXSI","TATAMTRDVR","TATAMOTORS","TATAPOWER","TATASTEEL","TECHM","RAMCOCEM","TITAN","TORNTPHARM","TORNTPOWER","TRENT","TIINDIA",
           "UPL","ULTRACEMCO","UNIONBANK","UBL","MCDOWELL_N","VBL","VEDL","IDEA","VOLTAS","WIPRO","YESBANK","ZEEL","ZOMATO","ZYDUSLIFE"]

strongBuyList = []
buyList = []
sellList = []
strongSellList = []
otherNutralList = []

class SymbSummary:
    strongBuyList = []
    buyList = []
    listOfBuys = []
    sellList = []
    listOfsells = []
    strongSellList = []
    otherNutralList = []

    def __init__(self):
        self.strongBuyList = []
        self.buyList = []
        self.listOfBuys = []
        self.sellList = []
        self.listOfsells = []
        self.strongSellList = []
        self.otherNutralList = []

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    # check length
    intersec = a_set.intersection(b_set)
    if len(intersec) > 0:
        return intersec
    else:
        return "no common elements"

def fillLists(symbSummary, interv):
    for symbol in symbols200:
        symb = TA_Handler(
            symbol=symbol,
            screener="india",
            exchange="NSE",
            interval=interv
        )
        summ = symb.get_analysis().summary
        # print(symbol + " - " + str(summ['RECOMMENDATION']))

        match summ['RECOMMENDATION']:
            case "STRONG_BUY":
                # symbSummary.strongBuyList.append(symbol + " - " + str(summ['RECOMMENDATION']))
                symbSummary.strongBuyList.append(symbol)
                symbSummary.listOfBuys.append(symbol)

            case "BUY":
                # symbSummary.buyList.append(symbol + " - " + str(summ['RECOMMENDATION']))
                symbSummary.buyList.append(symbol)
                symbSummary.listOfBuys.append(symbol)

            case "SELL":
                # symbSummary.sellList.append(symbol + " - " + str(summ['RECOMMENDATION']))
                symbSummary.sellList.append(symbol)
                symbSummary.listOfsells.append(symbol)

            case "STRONG_SELL":
                # symbSummary.strongSellList.append(symbol + " - " + str(summ['RECOMMENDATION']))
                symbSummary.strongSellList.append(symbol)
                symbSummary.listOfsells.append(symbol)

            case _:
                # symbSummary.otherNutralList.append(symbol + " - " + str(summ['RECOMMENDATION']))
                symbSummary.otherNutralList.append(symbol)




if __name__ == "__main__":
    symbSummary2H = SymbSummary()
    symbSummary4H = SymbSummary()

    fillLists(symbSummary2H, Interval.INTERVAL_2_HOURS)
    print("List filled with 2 Hours interval")
    fillLists(symbSummary4H, Interval.INTERVAL_4_HOURS)
    print("List filled with 4 Hours interval")

    setBuyList = common_member(symbSummary2H.listOfBuys, symbSummary4H.listOfBuys)

    print("Symbols with BUY signal")
    for symb in setBuyList:
        print("\t" + symb)

