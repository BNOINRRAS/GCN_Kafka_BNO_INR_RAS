from DType import *
import numpy  as np
import math, time
import julian

def form_LVC_url(bin_url_1, bin_url_2, bin_url_3, bin_url_4, bin_url_5, bin_url_6, bin_url_7, bin_url_8, bin_url_9, bin_url_10):
    all_parts = [bin_url_1, bin_url_2, bin_url_3, bin_url_4, bin_url_5, bin_url_6, bin_url_7, bin_url_8, bin_url_9, bin_url_10]
    LVC_url = ""
    for i in range(len(all_parts)):
        LVC_url = LVC_url + ''.join([chr(item) for item in reversed(all_parts[i])])
    LVC_url = LVC_url.rstrip('\x00')
    if LVC_url[len(LVC_url) - 1] == 't':#Временно пока так
        LVC_url = LVC_url + 's'#Временно пока так
#    print(LVC_url)
    return LVC_url

def SaveGcnMsg(data):
    with open("GCN.log",'a') as File:
        File.write(data[0]     +' '+
                   format(data[1],"8.2f") +' '+
                   format(data[2],"d")    +' '+
                   format(data[3],"8.2f") +' '+
                   format(data[4],"8.4f") +' '+
                   format(data[5],"8.4f") +' '+
                   format(data[6],"8.4f") +' '+
                   data[7]                +'\n')

def WriteToLogFile(String):
    LogString = (time.strftime("%y.%m.%d-%H:%M:%S", time.localtime())+' => '+String+'\n')
    with open('GCN_Kafka.log','a') as LogFile:
        LogFile.write(LogString)

def SaveGcnMsgBin(value, MsgType):
    binFileName = "BinaryMessage/GCN_"+MsgType+"_"+time.strftime("%y%m%d_%H-%M-%S", time.localtime())+".gcn"
    with open(binFileName, "wb") as binary_file: binary_file.write(value)


# (TYPE=53)+
def INTEGRAL_WAKEUP(value):
    np_data = np.frombuffer(value, dt_INTEGRAL_WAKEUP)
    if np_data['pkt_type'][0] != 53:
        WriteToLogFile('New INTEGRAL_WAKEUP notice, message.topic() != pkt_type')
        return(-1)
    if ((np_data['test_mpos'][0]>>31)&1) == 1:
        WriteToLogFile('New test INTEGRAL_WAKEUP notice')
        return(-1)
    else:
        WriteToLogFile('New INTEGRAL_WAKEUP notice')
        SaveGcnMsgBin(value, 'INTEGRAL_WAKEUP')
        h = math.floor(np_data['burst_sod'][0]/100/60/60)
        m = math.floor(np_data['burst_sod'][0]/100/60)-(h*60)
        s = math.floor(np_data['burst_sod'][0]/100) - (h*60+m)*60
        date = julian.from_jd((np_data['burst_tjd'][0]+ 2440000.5), fmt='jd')
        date = date.replace(hour=h,minute=m,second=s)
        data = [date.strftime('%Y-%m-%d.%H:%M:%S'),
                0,
                np_data['burst_tjd'][0],
                np_data['burst_sod'][0]/100, 
                np_data['burst_ra'][0]/10000, 
                np_data['burst_dec'][0]/10000, 
                np_data['burst_error'][0]/10000, 
                'INTEGRAL_WAKEUP']
        SaveGcnMsg(data)
        return(0)

# (TYPE=54)+
def INTEGRAL_REFINED(value):
    np_data = np.frombuffer(value, dt_INTEGRAL_REFINED)
    if np_data['pkt_type'][0] != 54:
        WriteToLogFile('New INTEGRAL_REFINED notice, message.topic() != pkt_type')
        return(-1)
    if ((np_data['test_mpos'][0]>>31)&1) == 1:
        WriteToLogFile('New test INTEGRAL_REFINED notice')
        return(-1)
    else:
        WriteToLogFile('New INTEGRAL_REFINED notice')
        SaveGcnMsgBin(value, 'INTEGRAL_REFINED')
        h = math.floor(np_data['burst_sod'][0]/100/60/60)
        m = math.floor(np_data['burst_sod'][0]/100/60)-(h*60)
        s = math.floor(np_data['burst_sod'][0]/100) - (h*60+m)*60
        date = julian.from_jd((np_data['burst_tjd'][0]+ 2440000.5), fmt='jd')
        date = date.replace(hour=h,minute=m,second=s)
        data = [date.strftime('%Y-%m-%d.%H:%M:%S'),
                0,
                np_data['burst_tjd'][0],
                np_data['burst_sod'][0]/100, 
                np_data['burst_ra'][0]/10000, 
                np_data['burst_dec'][0]/10000, 
                np_data['burst_error'][0]/10000, 
                'INTEGRAL_REFINED']
        SaveGcnMsg(data)
        return(0)

# (TYPE=55)+
def INTEGRAL_OFFLINE(value):
    np_data = np.frombuffer(value, dt_INTEGRAL_OFFLINE)
    if np_data['pkt_type'][0] != 55:
        WriteToLogFile('New INTEGRAL_OFFLINE notice, message.topic() != pkt_type')
        return(-1)
    if ((np_data['test_mpos'][0]>>31)&1) == 1: # TEST CHECK
        WriteToLogFile('New test INTEGRAL_OFFLINE notice')
        return(-1)
    else:
        WriteToLogFile('New INTEGRAL_OFFLINE notice')
        SaveGcnMsgBin(value, 'INTEGRAL_OFFLINE')
        h = math.floor(np_data['burst_sod'][0]/100/60/60)
        m = math.floor(np_data['burst_sod'][0]/100/60)-(h*60)
        s = math.floor(np_data['burst_sod'][0]/100) - (h*60+m)*60
        date = julian.from_jd((np_data['burst_tjd'][0]+ 2440000.5), fmt='jd')
        date = date.replace(hour=h,minute=m,second=s)
        data = [date.strftime('%Y-%m-%d.%H:%M:%S'),
                0,
                np_data['burst_tjd'][0],
                np_data['burst_sod'][0]/100, 
                np_data['burst_ra'][0]/10000, 
                np_data['burst_dec'][0]/10000, 
                np_data['burst_error'][0]/10000, 
                'INTEGRAL_OFFLINE']
        SaveGcnMsg(data)
        return(0)
 
# (TYPE=61)+
def SWIFT_BAT_GRB_POS_ACK(value):
    np_data = np.frombuffer(value, dt_SWIFT_BAT_GRB_POS_ACK)
    if np_data['pkt_type'][0] != 61:
        WriteToLogFile('New SWIFT_BAT_GRB_POS_ACK notice, message.topic() != pkt_type')
        return(-1)
    if ((np_data['soln_status'][0]>>30)&1) == 1:
        WriteToLogFile('New test SWIFT_BAT_GRB_POS_ACK notice')
        return(-1)
    else:
        WriteToLogFile('New SWIFT_BAT_GRB_POS_ACK notice')
        SaveGcnMsgBin(value, 'SWIFT_BAT_GRB_POS_ACK')
        h = math.floor(np_data['burst_sod'][0]/100/60/60)
        m = math.floor(np_data['burst_sod'][0]/100/60)-(h*60)
        s = math.floor(np_data['burst_sod'][0]/100) - (h*60+m)*60
        date = julian.from_jd((np_data['burst_tjd'][0] + 2440000.5), fmt='jd')
        date = date.replace(hour=h,minute=m,second=s)
        data = [date.strftime('%Y-%m-%d.%H:%M:%S'),
                0,
                np_data['burst_tjd'][0],
                np_data['burst_sod'][0]/100, 
                np_data['burst_ra'][0]/10000, 
                np_data['burst_dec'][0]/10000, 
                np_data['burst_error'][0]/10000, 
                'SWIFT_BAT_GRB_POS_ACK']
        SaveGcnMsg(data)
        return(0)

# (TYPE=111)
def FERMI_GBM_FLT_POS(value):
    np_data = np.frombuffer(value, dt_FERMI_GBM_FLT_POS)
    if np_data['pkt_type'][0] != 111:
        WriteToLogFile('New FERMI_GBM_FLT_POS notice, message.topic() != pkt_type')
        return(-1)
    if ((np_data['soln_status'][0]>>30)&1) == 1:
        WriteToLogFile('New test FERMI_GBM_FLT_POS notice')
        return(-1)
    else:
        WriteToLogFile('New FERMI_GBM_FLT_POS notice')
        SaveGcnMsgBin(value, 'FERMI_GBM_FLT_POS')
        h = math.floor(np_data['burst_sod'][0]/100/60/60)
        m = math.floor(np_data['burst_sod'][0]/100/60)-(h*60)
        s = math.floor(np_data['burst_sod'][0]/100) - (h*60+m)*60
        date = julian.from_jd((np_data['burst_tjd'][0] + 2440000.5), fmt='jd')
        date = date.replace(hour=h,minute=m,second=s)
        data = [date.strftime('%Y-%m-%d.%H:%M:%S'),
                0,
                np_data['burst_tjd'][0],
                np_data['burst_sod'][0]/100, 
                np_data['burst_ra'][0]/10000, 
                np_data['burst_dec'][0]/10000, 
                np_data['burst_error'][0]/10000, 
                'FERMI_GBM_FLT_POS']
        SaveGcnMsg(data)
        return(0)

# (TYPE=112)+
def FERMI_GBM_GND_POS(value):
    np_data = np.frombuffer(value, dt_FERMI_GBM_GND_POS)
    if np_data['pkt_type'][0] != 112:
        WriteToLogFile('New FERMI_GBM_GND_POS notice, message.topic() != pkt_type')
        return(-1)
    if ((np_data['soln_status'][0]>>30)&1) == 1:
        WriteToLogFile('New test FERMI_GBM_GND_POS notice')
        return(-1)
    else:
        WriteToLogFile('New FERMI_GBM_GND_POS notice')
        SaveGcnMsgBin(value, 'FERMI_GBM_GND_POS')
        h = math.floor(np_data['burst_sod'][0]/100/60/60)
        m = math.floor(np_data['burst_sod'][0]/100/60)-(h*60)
        s = math.floor(np_data['burst_sod'][0]/100) - (h*60+m)*60
        date = julian.from_jd((np_data['burst_tjd'][0] + 2440000.5), fmt='jd')
        date = date.replace(hour=h,minute=m,second=s)
        data = [date.strftime('%Y-%m-%d.%H:%M:%S'),
                0,
                np_data['burst_tjd'][0],
                np_data['burst_sod'][0]/100, 
                np_data['burst_ra'][0]/10000, 
                np_data['burst_dec'][0]/10000, 
                np_data['burst_error'][0]/10000, 
                'FERMI_GBM_GND_POS']
        SaveGcnMsg(data)
        return(0)

# (TYPE=115)+
def FERMI_GBM_FIN_POS(value):
    np_data = np.frombuffer(value, dt_FERMI_GBM_FIN_POS)
    if np_data['pkt_type'][0] != 115:
        WriteToLogFile('New FERMI_GBM_FIN_POS notice, message.topic() != pkt_type')
        return(-1)
    if ((np_data['soln_status'][0]>>30)&1) == 1:
        WriteToLogFile('New test FERMI_GBM_FIN_POS notice')
        return(-1)
    else:
        WriteToLogFile('New FERMI_GBM_FIN_POS notice')
        SaveGcnMsgBin(value, 'FERMI_GBM_FIN_POS')
        h = math.floor(np_data['burst_sod'][0]/100/60/60)
        m = math.floor(np_data['burst_sod'][0]/100/60)-(h*60)
        s = math.floor(np_data['burst_sod'][0]/100) - (h*60+m)*60
        date = julian.from_jd((np_data['burst_tjd'][0] + 2440000.5), fmt='jd')
        date = date.replace(hour=h,minute=m,second=s)
        data = [date.strftime('%Y-%m-%d.%H:%M:%S'),
                0,
                np_data['burst_tjd'][0],
                np_data['burst_sod'][0]/100, 
                np_data['burst_ra'][0]/10000, 
                np_data['burst_dec'][0]/10000, 
                np_data['burst_error'][0]/10000, 
                'FERMI_GBM_FIN_POS']
        SaveGcnMsg(data)
        return(0)

# (TYPE=128)+
def FERMI_LAT_OFFLINE(value):
    np_data = np.frombuffer(value, dt_FERMI_LAT_OFFLINE)
    if np_data['pkt_type'][0] != 128:
        WriteToLogFile('New FERMI_LAT_OFFLINE notice, message.topic() != pkt_type')
        return(-1)
    if ((np_data['Trig_ID'][0]>>30)&1) == 1:
        WriteToLogFile('New test FERMI_LAT_OFFLINE notice')
        return(-1)
    else:
        WriteToLogFile('New FERMI_LAT_OFFLINE notice')
        SaveGcnMsgBin(value, 'FERMI_GBM_FIN_POS')
        h = math.floor(np_data['trig_sod'][0]/100/60/60)
        m = math.floor(np_data['trig_sod'][0]/100/60)-(h*60)
        s = math.floor(np_data['trig_sod'][0]/100) - (h*60+m)*60
        date = julian.from_jd((np_data['burst_tjd'][0] + 2440000.5), fmt='jd')
        date = date.replace(hour=h,minute=m,second=s)
        data = [date.strftime('%Y-%m-%d.%H:%M:%S'),
                0,
                np_data['trig_tjd'][0],
                np_data['trig_sod'][0]/100, 
                np_data['burst_ra'][0]/10000, 
                np_data['burst_dec'][0]/10000, 
                np_data['burst_error'][0]/10000, 
                'FERMI_LAT_OFFLINE']
        SaveGcnMsg(data)
        return(0)

# (TYPE=149)+
def SNEWS(value):
    np_data = np.frombuffer(value, dt_SNEWS)
    if np_data['pkt_type'][0] != 149:
        WriteToLogFile('New SNEWS notice, message.topic() != pkt_type')
        return(-1)
    if ((np_data['trig_id'][0]>>1)&1) == 1:
        WriteToLogFile('New test SNEWS notice')
        return(-1)
    else:
        WriteToLogFile('New SNEWS notice')
        SaveGcnMsgBin(value, 'SNEWS')
        h = math.floor(np_data['event_sod'][0]/100/60/60)
        m = math.floor(np_data['event_sod'][0]/100/60)-(h*60)
        s = math.floor(np_data['event_sod'][0]/100) - (h*60+m)*60
        date = julian.from_jd((np_data['event_tjd'][0] + 2440000.5), fmt='jd')
        date = date.replace(hour=h,minute=m,second=s)
        data = [date.strftime('%Y-%m-%d.%H:%M:%S'),
                0,
                np_data['event_tjd'][0],
                np_data['event_sod'][0]/100, 
                np_data['event_ra'][0]/10000, 
                np_data['event_dec'][0]/10000, 
                np_data['event_error'][0]/10000, 
                'SNEWS']
        SaveGcnMsg(data)
        return(0)

# (TYPE=151)+
def LVC_INITIAL(value):
    np_data = np.frombuffer(value, dt_LVC_INITIAL)
    if np_data['pkt_type'][0] != 151:
        WriteToLogFile('New LVC_INITIAL notice, message.topic() != pkt_type')
        return(-1)
    if ((np_data['trig_id'][0]>>1)&1) == 1:
        WriteToLogFile('New test LVC_INITIAL notice')
        return(-1)
    else:
        WriteToLogFile('New LVC_INITIAL notice')
        SaveGcnMsgBin(value, 'LVC_INITIAL')
        h = math.floor(np_data['event_sod'][0]/100/60/60)
        m = math.floor(np_data['event_sod'][0]/100/60)-(h*60)
        s = math.floor(np_data['event_sod'][0]/100) - (h*60+m)*60
        date = julian.from_jd((np_data['event_tjd'][0] + 2440000.5), fmt='jd')
        date = date.replace(hour=h,minute=m,second=s)
        data = [date.strftime('%Y-%m-%d.%H:%M:%S'),
                0,
                np_data['event_tjd'][0],
                np_data['event_sod'][0]/100, 
                0, # there no RA in LVC_RETRACTION
                0, # there no Dec in LVC_RETRACTION
                0, # there no Error in LVC_RETRACTION
                ('LVC_INITIAL ' + form_LVC_url(np_data['url_1'][0], np_data['url_2'][0], np_data['url_3'][0],
                                                   np_data['url_4'][0], np_data['url_5'][0], np_data['url_6'][0],
                                                   np_data['url_7'][0], np_data['url_8'][0], np_data['url_9'][0],
                                                   np_data['url_10'][0]))]
        SaveGcnMsg(data)
    return(0)

# (TYPE=152)+
def LVC_UPDATE(value):
    np_data = np.frombuffer(value, dt_LVC_UPDATE)
    if np_data['pkt_type'][0] != 152:
        WriteToLogFile('New LVC_UPDATE notice, message.topic() != pkt_type')
        return(-1)
    if ((np_data['trig_id'][0]>>1)&1) == 1:
        WriteToLogFile('New test LVC_UPDATE notice')
        return(-1)
    else:
        WriteToLogFile('New LVC_UPDATE notice')
        SaveGcnMsgBin(value, 'LVC_UPDATE')
        h = math.floor(np_data['event_sod'][0]/100/60/60)
        m = math.floor(np_data['event_sod'][0]/100/60)-(h*60)
        s = math.floor(np_data['event_sod'][0]/100) - (h*60+m)*60
        date = julian.from_jd((np_data['event_tjd'][0] + 2440000.5), fmt='jd')
        date = date.replace(hour=h,minute=m,second=s)
        data = [date.strftime('%Y-%m-%d.%H:%M:%S'),
                0,
                np_data['event_tjd'][0],
                np_data['event_sod'][0]/100, 
                0, # there no RA in LVC_RETRACTION
                0, # there no Dec in LVC_RETRACTION
                0, # there no Error in LVC_RETRACTION
                ('LVC_UPDATE ' + form_LVC_url(np_data['url_1'][0], np_data['url_2'][0], np_data['url_3'][0],
                                                   np_data['url_4'][0], np_data['url_5'][0], np_data['url_6'][0],
                                                   np_data['url_7'][0], np_data['url_8'][0], np_data['url_9'][0],
                                                   np_data['url_10'][0]))]
        SaveGcnMsg(data)
    return(0)
    
# (TYPE=150)+
def LVC_PRELIMINARY(value):
    np_data = np.frombuffer(value, dt_LVC_PRELIMINARY)
    if np_data['pkt_type'][0] != 150:
        WriteToLogFile('New LVC_PRELIMINARY notice, message.topic() != pkt_type')
        return(-1)
    if ((np_data['trig_id'][0]>>1)&1) == 1:
        WriteToLogFile('New test LVC_PRELIMINARY notice')
        return(-1)
    else:
        WriteToLogFile('New LVC_PRELIMINARY notice')
        SaveGcnMsgBin(value, 'LVC_PRELIMINARY')
        h = math.floor(np_data['event_sod'][0]/100/60/60)
        m = math.floor(np_data['event_sod'][0]/100/60)-(h*60)
        s = math.floor(np_data['event_sod'][0]/100) - (h*60+m)*60
        date = julian.from_jd((np_data['event_tjd'][0] + 2440000.5), fmt='jd')
        date = date.replace(hour=h,minute=m,second=s)
        data = [date.strftime('%Y-%m-%d.%H:%M:%S'),
                0,
                np_data['event_tjd'][0],
                np_data['event_sod'][0]/100, 
                0, # there no RA in LVC_RETRACTION
                0, # there no Dec in LVC_RETRACTION
                0, # there no Error in LVC_RETRACTION
                ('LVC_PRELIMINARY ' + form_LVC_url(np_data['url_1'][0], np_data['url_2'][0], np_data['url_3'][0],
                                                   np_data['url_4'][0], np_data['url_5'][0], np_data['url_6'][0],
                                                   np_data['url_7'][0], np_data['url_8'][0], np_data['url_9'][0],
                                                   np_data['url_10'][0]))]
        SaveGcnMsg(data)
    return(0)

# (TYPE=164)
def LVC_RETRACTION(value):
    np_data = np.frombuffer(value, dt_LVC_RETRACTION)
    if np_data['pkt_type'][0] != 164:
        WriteToLogFile('New LVC_RETRACTION notice, message.topic() != pkt_type')
        return(-1)
    if ((np_data['trig_id'][0]>>1)&1) == 1:
        WriteToLogFile('New test LVC_RETRACTION notice')
        return(-1)
    else:
        WriteToLogFile('New LVC_RETRACTION notice')
        SaveGcnMsgBin(value, 'LVC_RETRACTION')
        h = math.floor(np_data['event_sod'][0]/100/60/60)
        m = math.floor(np_data['event_sod'][0]/100/60)-(h*60)
        s = math.floor(np_data['event_sod'][0]/100) - (h*60+m)*60
        date = julian.from_jd((np_data['event_tjd'][0] + 2440000.5), fmt='jd')
        date = date.replace(hour=h,minute=m,second=s)
        data = [date.strftime('%Y-%m-%d.%H:%M:%S'),
                0,
                np_data['event_tjd'][0],
                np_data['event_sod'][0]/100, 
                0, # there no RA in LVC_RETRACTION
                0, # there no Dec in LVC_RETRACTION
                0, # there no Error in LVC_RETRACTION
                'LVC_RETRACTION']
        SaveGcnMsg(data)
        return(0)

# (TYPE=171)+
def HAWC_BURST_MONITOR(value):
    np_data = np.frombuffer(value, dt_HAWC_BURST_MONITOR)
    if np_data['pkt_type'][0] != 171:
        WriteToLogFile('New HAWC_BURST_MONITOR notice, message.topic() != pkt_type')
        return(-1)
    if ((np_data['trig_id'][0]>>1)&1) == 1:
        WriteToLogFile('New test HAWC_BURST_MONITOR notice')
        return(-1)
    else:
        WriteToLogFile('New HAWC_BURST_MONITOR notice')
        SaveGcnMsgBin(value, 'HAWC_BURST_MONITOR')
        h = math.floor(np_data['event_sod'][0]/100/60/60)
        m = math.floor(np_data['event_sod'][0]/100/60)-(h*60)
        s = math.floor(np_data['event_sod'][0]/100) - (h*60+m)*60
        date = julian.from_jd((np_data['event_tjd'][0] + 2440000.5), fmt='jd')
        date = date.replace(hour=h,minute=m,second=s)
        data = [date.strftime('%Y-%m-%d.%H:%M:%S'),
                0,
                np_data['event_tjd'][0],
                np_data['event_sod'][0]/100, 
                np_data['event_ra'][0]/10000, 
                np_data['event_dec'][0]/10000, 
                np_data['evt_error'][0]/10000, 
                'HAWC_BURST_MONITOR']
        SaveGcnMsg(data)
        return(0)

# (TYPE=172)
def AMON_NU_EM_COINC (value):
    np_data = np.frombuffer(value, dt_AMON_NU_EM_COINC)
    if np_data['pkt_type'][0] != 172:
        WriteToLogFile('New AMON_NU_EM_COINC notice, message.topic() != pkt_type')
        return(-1)
    return(0)

# (TYPE=173)+
def ICECUBE_ASTROTRACK_GOLD(value):
    np_data = np.frombuffer(value, dt_ICECUBE_ASTROTRACK_GOLD)
    if np_data['pkt_type'][0] != 173:
        WriteToLogFile('New ICECUBE_ASTROTRACK_GOLD notice, message.topic() != pkt_type')
        return(-1)
    if ((np_data['trig_id'][0]>>1)&1) == 1:
        WriteToLogFile('New test ICECUBE_ASTROTRACK_GOLD notice')
        return(-1)
    else:
        WriteToLogFile('New ICECUBE_ASTROTRACK_GOLD notice')
        SaveGcnMsgBin(value, 'ICECUBE_ASTROTRACK_GOLD')
        h = math.floor(np_data['event_sod'][0]/100/60/60)
        m = math.floor(np_data['event_sod'][0]/100/60)-(h*60)
        s = math.floor(np_data['event_sod'][0]/100) - (h*60+m)*60
        date = julian.from_jd((np_data['event_tjd'][0] + 2440000.5), fmt='jd')
        date = date.replace(hour=h,minute=m,second=s)
        data = [date.strftime('%Y-%m-%d.%H:%M:%S'),
                0,
                np_data['event_tjd'][0],
                np_data['event_sod'][0]/100, 
                np_data['event_ra'][0]/10000, 
                np_data['event_dec'][0]/10000, 
                np_data['evt_error90'][0]/10000, 
                'ICECUBE_ASTROTRACK_GOLD']
        SaveGcnMsg(data)
        return(0)

# (TYPE=174)+
def ICECUBE_ASTROTRACK_BRONZE(value):
    np_data = np.frombuffer(value, dt_ICECUBE_ASTROTRACK_BRONZE)
    if np_data['pkt_type'][0] != 174:
        WriteToLogFile('New ICECUBE_ASTROTRACK_BRONZE notice, message.topic() != pkt_type')
        return(-1)
    if ((np_data['trig_id'][0]>>1)&1) == 1:
        WriteToLogFile('New test ICECUBE_ASTROTRACK_BRONZE notice')
        return(-1)
    else:
        WriteToLogFile('New ICECUBE_ASTROTRACK_BRONZE notice')
        SaveGcnMsgBin(value, 'ICECUBE_ASTROTRACK_BRONZE')
        h = math.floor(np_data['event_sod'][0]/100/60/60)
        m = math.floor(np_data['event_sod'][0]/100/60)-(h*60)
        s = math.floor(np_data['event_sod'][0]/100) - (h*60+m)*60
        date = julian.from_jd((np_data['event_tjd'][0] + 2440000.5), fmt='jd')
        date = date.replace(hour=h,minute=m,second=s)
        data = [date.strftime('%Y-%m-%d.%H:%M:%S'),
                0,
                np_data['event_tjd'][0],
                np_data['event_sod'][0]/100, 
                np_data['event_ra'][0]/10000, 
                np_data['event_dec'][0]/10000, 
                np_data['evt_error90'][0]/10000, 
                'ICECUBE_ASTROTRACK_BRONZE']
        SaveGcnMsg(data)
        return(0)

# (TYPE=176)+
def AMON_ICECUBE_CASCADE(value):
    np_data = np.frombuffer(value, dt_AMON_ICECUBE_CASCADE)
    if np_data['pkt_type'][0] != 176:
        WriteToLogFile('New AMON_ICECUBE_CASCADE notice, message.topic() != pkt_type')
        return(-1)
    if ((np_data['trig_id'][0]>>1)&1) == 1:
        WriteToLogFile('New test AMON_ICECUBE_CASCADE notice')
        return(-1)
    else:
        WriteToLogFile('New AMON_ICECUBE_CASCADE notice')
        SaveGcnMsgBin(value, 'AMON_ICECUBE_CASCADE')
        h = math.floor(np_data['event_sod'][0]/100/60/60)
        m = math.floor(np_data['event_sod'][0]/100/60)-(h*60)
        s = math.floor(np_data['event_sod'][0]/100) - (h*60+m)*60
        date = julian.from_jd((np_data['event_tjd'][0] + 2440000.5), fmt='jd')
        date = date.replace(hour=h,minute=m,second=s)
        data = [date.strftime('%Y-%m-%d.%H:%M:%S'),
                0,
                np_data['event_tjd'][0],
                np_data['event_sod'][0]/100,
                np_data['ra'][0]/10000,
                np_data['dec'][0]/10000,
                np_data['pos_error_90'][0]/10000,
                'AMON_ICECUBE_CASCADE']
        SaveGcnMsg(data)
        return(0)
    



