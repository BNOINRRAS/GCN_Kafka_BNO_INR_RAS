from GCN_Consumer import *
from gcn_kafka import Consumer

import threading
import os
import signal

# Connect as a consumer. Warning: don't share the client secret with others.
consumer = Consumer(client_id='',
                    client_secret='')

# Subscribe to topics and receive alerts
consumer.subscribe(['gcn.classic.binary.INTEGRAL_WAKEUP',
                    'gcn.classic.binary.INTEGRAL_REFINED',
                    'gcn.classic.binary.INTEGRAL_OFFLINE',
                    'gcn.classic.binary.FERMI_GBM_FLT_POS',
                    'gcn.classic.binary.FERMI_GBM_GND_POS',
                    'gcn.classic.binary.FERMI_GBM_FIN_POS',
                    'gcn.classic.binary.FERMI_LAT_OFFLINE',
                    'gcn.classic.binary.SWIFT_BAT_GRB_POS_ACK',
                    'gcn.classic.binary.HAWC_BURST_MONITOR',
                    'gcn.classic.binary.ICECUBE_ASTROTRACK_BRONZE',
                    'gcn.classic.binary.ICECUBE_ASTROTRACK_GOLD',
                    'gcn.classic.binary.ICECUBE_CASCADE',
                    'gcn.classic.binary.SNEWS',
                    'gcn.classic.binary.LVC_INITIAL',
                    'gcn.classic.binary.LVC_UPDATE',
                    'gcn.classic.binary.LVC_PRELIMINARY'
                    ])

# --------- Timer for checking settings
def run_every_n_seconds(seconds, action, *args):
    threading.Timer(seconds, run_every_n_seconds, [seconds, action] + list(args)).start()
    action(*args)

def timer_task():
    settingsFile = open('settings', 'r')
    linesRunTheProgram = settingsFile.readlines()
    for line in linesRunTheProgram:
        key, value = line.strip().split('\t')
        # keyRunTheProgram = key
        valueRunTheProgram = value
        print(valueRunTheProgram)
    settingsFile.close()
    if valueRunTheProgram != 'y':
        print('Exiting the program')
        os.kill(os.getpid(), signal.SIGINT)

run_every_n_seconds(5, timer_task)
# ---------

while True:
    for message in consumer.consume(timeout=1):
        if message.error():
            WriteToLogFile(message.error())
            continue
        data = 1
        if len(message.value()) == 160:
            if   message.topic() == 'gcn.classic.binary.INTEGRAL_WAKEUP':          data = INTEGRAL_WAKEUP(message.value())               # +
            elif message.topic() == 'gcn.classic.binary.INTEGRAL_REFINED':         data = INTEGRAL_REFINED(message.value())              # +
            elif message.topic() == 'gcn.classic.binary.INTEGRAL_OFFLINE':         data = INTEGRAL_OFFLINE(message.value())              # +
            elif message.topic() == 'gcn.classic.binary.FERMI_GBM_FLT_POS':        data = FERMI_GBM_FLT_POS(message.value())             # +
            elif message.topic() == 'gcn.classic.binary.FERMI_GBM_GND_POS':        data = FERMI_GBM_GND_POS(message.value())             # +
            elif message.topic() == 'gcn.classic.binary.FERMI_GBM_FIN_POS':        data = FERMI_GBM_FIN_POS(message.value())             # +
            elif message.topic() == 'gcn.classic.binary.FERMI_LAT_OFFLINE':        data = FERMI_LAT_OFFLINE(message.value())             # +
            elif message.topic() == 'gcn.classic.binary.SWIFT_BAT_GRB_POS_ACK':    data = SWIFT_BAT_GRB_POS_ACK(message.value())         # +
            elif message.topic() == 'gcn.classic.binary.HAWC_BURST_MONITOR':       data = HAWC_BURST_MONITOR(message.value())            # +
            elif message.topic() == 'gcn.classic.binary.ICECUBE_ASTROTRACK_BRONZE':data = ICECUBE_ASTROTRACK_BRONZE(message.value())     # +
            elif message.topic() == 'gcn.classic.binary.ICECUBE_ASTROTRACK_GOLD':  data = ICECUBE_ASTROTRACK_GOLD(message.value())       # +
            elif message.topic() == 'gcn.classic.binary.ICECUBE_CASCADE':          data = AMON_ICECUBE_CASCADE(message.value())          # +
            elif message.topic() == 'gcn.classic.binary.SNEWS':                    data = SNEWS(message.value())                         # +
            elif message.topic() == 'gcn.classic.binary.LVC_INITIAL':              data = LVC_INITIAL(message.value())                   # +
            elif message.topic() == 'gcn.classic.binary.LVC_UPDATE':               data = LVC_UPDATE(message.value())                    # +
            elif message.topic() == 'gcn.classic.binary.LVC_PRELIMINARY':          data = LVC_PRELIMINARY(message.value())               # +
