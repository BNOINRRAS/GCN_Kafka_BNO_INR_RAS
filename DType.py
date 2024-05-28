import numpy  as np

#https://gcn.gsfc.nasa.gov/sock_pkt_def_doc.html

# (TYPE=53)
dt_INTEGRAL_WAKEUP = np.dtype([
        ('pkt_type'    ,'>i4'),       # integer         Packet type number (=53)
        ('pkt_sernum'  ,'>i4'),       # integer         1 thru infinity
        ('pkt_hop_cnt' ,'>i4'),       # integer         Incremented by each node
        ('pkt_sod'     ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('trig_sub_num','>i4'),       # integers        Trigger num & mesg sernum
        ('burst_tjd'   ,'>i4'),       # [days]          Truncated Julian Day
        ('burst_sod'   ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('burst_ra'    ,'>i4'),       # [10^-4-deg]     (int)(0.0 to 359.9999 *10000)
        ('burst_dec'   ,'>i4'),       # (int)(-90.0 to +90.0 *10000)
        ('det_flags'   ,'>i4'),       # bits            Detector flag bits
        ('inten_sigma' ,'>i4'),       # [centi-sigma]   Burst_intensity_sigma*100
        ('burst_error' ,'>i4'),       # [arcsec]        Burst location uncertainty
        ('test_mpos'   ,'>i4'),       # flag_bits       Test and Multi-Position flags
        ('time_scale'  ,'>i4'),       # [10^-4 sec]     Time sampling or trigger time
        ('sc_ra'       ,'>i4'),       # [10^-4-deg]     (int)(0.0 to 359.9999 *10000)
        ('sc_dec'      ,'>i4'),       # [10^-4-deg]     (int)(-90.0 to +90.0 *10000)
        ('time_error'  ,'>i4'),       # [10^-4 sec]     Accuracy of GRB time
        ('spare0'      ,'(1,2)>i4'),  # integer         8 bytes for the future
        ('misc_att'    ,'>i4'),       # integer         S/c status & attitude
        ('spare1'      ,'(1,19)>i4'), # integer         76 bytes for the future
        ('pkt_term'    ,'>i4')        # integer         Pkt Termination (always = \n)
    ])

# (TYPE=54)
dt_INTEGRAL_REFINED = np.dtype([
        ('pkt_type'    ,'>i4'),       # integer         Packet type number (=54)
        ('pkt_sernum'  ,'>i4'),       # integer         1 thru infinity
        ('pkt_hop_cnt' ,'>i4'),       # integer         Incremented by each node
        ('pkt_sod'     ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('trig_sub_num','>i4'),       # integers        Trigger num & mesg sernum
        ('burst_tjd'   ,'>i4'),       # [days]          Truncated Julian Day
        ('burst_sod'   ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('burst_ra'    ,'>i4'),       # [10^-4-deg]     (int)(0.0 to 359.9999 *10000)
        ('burst_dec'   ,'>i4'),       # [10^-4-deg]     (int)(-90.0 to +90.0 *10000)
        ('det_flags'   ,'>i4'),       # bits            Detector flag bits
        ('inten_sigma' ,'>i4'),       # [centi-sigma]   Burst_intensity_sigma*100
        ('burst_error' ,'>i4'),       # [arcsec]        Burst location uncertainty
        ('test_mpos'   ,'>i4'),       # flag_bits       Test and Multi-Position flags
        ('time_scale'  ,'>i4'),       # [10^-4 sec]     Time sampling or trigger time
        ('sc_ra'       ,'>i4'),       # [10^-4-deg]     (int)(0.0 to 359.9999 *10000)
        ('sc_dec'      ,'>i4'),       # [10^-4-deg]     (int)(-90.0 to +90.0 *10000)
        ('time_error'  ,'>i4'),       # [10^-4 sec]     Accuracy of GRB time
        ('spare0'      ,'(1,2)>i4'),  # integer         8 bytes for the future
        ('misc_att'    ,'>i4'),       # integer         S/c status & attitude
        ('spare1'      ,'(1,19)>i4'), # integer         76 bytes for the future
        ('pkt_term'    ,'>i4')        # integer         Pkt Termination (always = \n)
    ])

# (TYPE=55)
dt_INTEGRAL_OFFLINE = np.dtype([
        ('pkt_type'    ,'>i4'),       # integer         Packet type number (=55)
        ('pkt_sernum'  ,'>i4'),       # integer         1 thru infinity
        ('pkt_hop_cnt' ,'>i4'),       # integer         Incremented by each node
        ('pkt_sod'     ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('trig_sub_num','>i4'),       # integers        Trigger num & mesg sernum
        ('burst_tjd'   ,'>i4'),       # [days]          Truncated Julian Day
        ('burst_sod'   ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('burst_ra'    ,'>i4'),       # [10^-4-deg]     (int)(0.0 to 359.9999 *10000)
        ('burst_dec'   ,'>i4'),       # [10^-4-deg]     (int)(-90.0 to +90.0 *10000)
        ('det_flags'   ,'>i4'),       # bits            Detector flag bits
        ('inten_sigma' ,'>i4'),       # [centi-sigma]   Burst_intensity_sigma*100
        ('burst_error' ,'>i4'),       # [arcsec]        Burst location uncertainty
        ('test_mpos'   ,'>i4'),       # flag_bits       Test and Multi-Position flags
        ('time_scale'  ,'>i4'),       # [10^-4 sec]     Time sampling or trigger time
        ('sc_ra'       ,'>i4'),       # [10^-4-deg]     (int)(0.0 to 359.9999 *10000)
        ('sc_dec'      ,'>i4'),       # [10^-4-deg]     (int)(-90.0 to +90.0 *10000)
        ('time_error'  ,'>i4'),       # [10^-4 sec]     Accuracy of GRB time
        ('spare0'      ,'(1,2)>i4'),  # integer         8 bytes for the future
        ('misc_att'    ,'>i4'),       # integer         S/c status & attitude
        ('spare'       ,'(1,19)>i4'), # integer         76 bytes for the future
        ('pkt_term'    ,'>i4')        # integer         Pkt Termination (always = \n)
    ])

# (TYPE=61)
dt_SWIFT_BAT_GRB_POS_ACK = np.dtype([
        ('pkt_type'    ,'>i4'),       # integer         Packet type number (=61)
        ('pkt_sernum'  ,'>i4'),       # integer         1 thru infinity
        ('pkt_hop_cnt' ,'>i4'),       # integer         Incremented by each node
        ('pkt_sod'     ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('trig_obs_num','>i4'),       # integers        Trigger num & Observation num
        ('burst_tjd'   ,'>i4'),       # [days]          Truncated Julian Day
        ('burst_sod'   ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('burst_ra'    ,'>i4'),       # [0.0001-deg]    (int)(0.0 to 359.9999 *10000)
        ('burst_dec'   ,'>i4'),       # [0.0001-deg]    (int)(-90.0 to +90.0 *10000)
        ('burst_flue'  ,'>i4'),       # [counts]        Num events during trig window, 0 to inf
        ('burst_ipeak' ,'>i4'),       # [cnts*ff]       Counts in image-plane peak, 0 to infinity
        ('burst_error' ,'>i4'),       # [0.0001-deg]    (int)(0.0 to 180.0 *10000)
        ('phi'         ,'>i4'),       # [centi-deg]     (int)(0.0 to 359.9999 *100)
        ('theta'       ,'>i4'),       # [centi-deg]     (int)(0.0 to +70.0 *100)
        ('integ_time'  ,'>i4'),       # [4mSec]         Duration of the trigger interval, 1 to inf
        ('spare0'      ,'>i4'),       # integer         4 bytes for the future
        ('lon_lat'     ,'>i4'),       # 2_shorts        (int)(Longitude,Lattitude *100)
        ('trig_index'  ,'>i4'),       # integer         Rate_Trigger index
        ('soln_status' ,'>i4'),       # bits            Type of source/trigger found
        ('misc'        ,'>i4'),       # bits            Misc stuff packed in here
        ('image_signif','>i4'),       # [centi-sigma]   (int)(sig2noise *100)
        ('rate_signif' ,'>i4'),       # [centi-sigma]   (int)(sig2noise *100)
        ('bkg_flue'    ,'>i4'),       # [counts]        Num events during the bkg interval, 0 to inf
        ('bkg_start'   ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('bkg_dur'     ,'>i4'),       # [centi-sec]     (int)(0-80,000 *100)
        ('cat_num'     ,'>i4'),       # integer         On-board cat match ID number
        ('spare1'      ,'(1,10)>i4'), # integer         40 bytes for the future
        ('merit_0_3'   ,'>i4'),       # integers        Merit params 0,1,2,3 (-127 to +127)
        ('merit_4_7'   ,'>i4'),       # integers        Merit params 4,5,6,7 (-127 to +127)
        ('merit_8_9'   ,'>i4'),       # integers        Merit params 8,9     (-127 to +127)
        ('pkt_term'    ,'>i4')        # integer         Pkt Termination (always = \n)
    ])

# (TYPE=111)
dt_FERMI_GBM_FLT_POS = np.dtype([
        ('pkt_type'    ,'>i4'),      # integer         Packet type number (=111 or 117)
        ('pkt_sernum'  ,'>i4'),      # integer         1 thru infinity
        ('pkt_hop_cnt' ,'>i4'),      # integer         Incremented by each node
        ('pkt_sod'     ,'>i4'),      # [centi-sec]     (int)(sssss.sss *100)
        ('trig_num'    ,'>i4'),      # integer         Trigger number
        ('burst_tjd'   ,'>i4'),      # [days]          Truncated Julian Day
        ('burst_sod'   ,'>i4'),      # [centi-sec]     (int)(sssss.sss *100)
        ('burst_ra'    ,'>i4'),      # [0.0001-deg]    (int)(0.0 to 359.9999 *10000)
        ('burst_dec'   ,'>i4'),      # [0.0001-deg]    (int)(-90.0 to +90.0 *10000)
        ('burst_flue'  ,'>i4'),      # [counts]        Num events during trig window, 0 to inf
        ('spare0'      ,'>i4'),      # integer         4 bytes for the future
        ('burst_error' ,'>i4'),      # [0.0001-deg]    (int)(0.0 to 180.0 *10000)
        ('phi'         ,'>i4'),      # [centi-deg]     (int)(0.0 to 359.9999 *100)
        ('theta'       ,'>i4'),      # [centi-deg]     (int)(0.0 to +100.0 *100)
        ('trigTmScale' ,'>i4'),      # [milli-sec]     Trigger Time Scale
        ('spare1'      ,'(1,2)>i4'), # integer         8 bytes for the future
        ('dataTmScale' ,'>i4'),      # [milli-sec]     Data Time Scale
        ('soln_status' ,'>i4'),      # bits            Type of source/trigger found
        ('misc'        ,'>i4'),      # bits            Misc stuff packed in here
        ('rec_seq_num' ,'>i4'),      # integer         SerNum of the messages (1-~40)
        ('data_signif' ,'>i4'),      # [centi-sigma]   (int)(sig2noise *100)
        ('loc_algor'   ,'>i4'),      # integer         Location algorithm (1-???)
        ('most_likely' ,'>i4'),      # integer         Mostly class ID & probability
        ('most_likely2','>i4'),      # integer         2nd Mostly class ID & probability
        ('hard_ratio'  ,'>i4'),      # [centi-dn]      (int)(hardness_ratio *100)
        ('dets'        ,'>i4'),      # bits            The 2 dets that triggered
        ('spare2'      ,'(1,4)>i4'), # integers        20 bytes for the future
        ('lc_yymmdd'   ,'>i4'),      # integer         The YYMMDD for the lc_url
        ('lc_fff'      ,'>i4'),      # integer         The FFF fraction-of-day for the lc_url
        ('spare3'      ,'(1,4)>i4'), # integer         16 bytes for the future
        ('longitude'   ,'>i4'),      # [arcmin]        Geo (East) Longitude of s/c
        ('latitude'    ,'>i4'),      # [arcmin]        Geo Latitude of s/c
        ('pkt_term'    ,'>i4')       # integer         Pkt Termination (always = \n)
    ])

# (TYPE=112)
dt_FERMI_GBM_GND_POS = np.dtype([
        ('pkt_type'     ,'>i4'),      # integer         Packet type number (=112)
        ('pkt_sernum'   ,'>i4'),      # integer         1 thru infinity
        ('pkt_hop_cnt'  ,'>i4'),      # integer         Incremented by each node
        ('pkt_sod'      ,'>i4'),      # [centi-sec]     (int)(sssss.sss *100)
        ('trig_num'     ,'>i4'),      # integer         Trigger number
        ('burst_tjd'    ,'>i4'),      # [days]          Truncated Julian Day
        ('burst_sod'    ,'>i4'),      # [centi-sec]     (int)(sssss.sss *100)
        ('burst_ra'     ,'>i4'),      # [0.0001-deg]    (int)(0.0 to 359.9999 *10000)
        ('burst_dec'    ,'>i4'),      # [0.0001-deg]    (int)(-90.0 to +90.0 *10000)
        ('spare0'       ,'(1,2)>i4'), # integers        8 bytes for the future
        ('burst_error'  ,'>i4'),      # [0.0001-deg]    (int)(0.0 to 180.0 *10000)
        ('phi'          ,'>i4'),      # [centi-deg]     (int)(0.0 to 359.9999 *100)
        ('theta'        ,'>i4') ,     # [centi-deg]     (int)(0.0 to +100.0 *100)
        ('data_interval','>i4'),      # [milli-sec]     Duration of the trigger interval, 1 to inf
        ('spare1'       ,'>i4'),      # integer         4 bytes for the future
        ('lon_lat'      ,'>i4'),      # integer         Longitude, Lattitude
        ('spare2'       ,'>i4'),      # integer         4 bytes for the future
        ('soln_status'  ,'>i4'),      # bits            Type of source/trigger found
        ('misc'         ,'>i4'),      # bits            Misc stuff packed in here
        ('rec_seq_num'  ,'>i4'),      # integer         SerNum of the messages (1-~40)
        ('burst_signif' ,'>i4'),      # [deci-sigma]    (int)(sig2noise *10)
        ('loc_algor'    ,'>i4'),      # integer         Location algorithm (1-???)
        ('spare3'       ,'(1,3)>i4'), # integers        12 bytes for the future
        ('lo_E'         ,'>i4'),      # integer         E_range_lo *1000 keV
        ('hi_E'         ,'>i4'),      # integer         E_range_hi *1000 keV
        ('sc_x'         ,'>i4'),      # integer         X-coordinate of s/c *4.0 km
        ('sc_y'         ,'>i4'),      # Y-coordinate of s/c *4.0 km
        ('sc_z'         ,'>i4'),      # integer         Z-coordinate of s/c *4.0 km
        ('lc_yymmdd'    ,'>i4'),      # integer         The YYMMDD for the lc_url
        ('lc_fff'       ,'>i4'),      # integer         The FFF fraction-of-day for the lc_url
        ('spare4'       ,'(1,6)>i4'), # integer         24 bytes for the future
        ('pkt_term'     ,'>i4')       # integer         Pkt Termination (always = \n)
    ])

# (TYPE=115)
dt_FERMI_GBM_FIN_POS = np.dtype([
        ('pkt_type'   ,'>i4'),       # integer         Packet type number (=115)
        ('pkt_sernum' ,'>i4'),       # integer         1 thru infinity
        ('pkt_hop_cnt','>i4'),       # integer         Incremented by each node
        ('pkt_sod'    ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('trig_num'   ,'>i4'),       # integer         Trigger number
        ('burst_tjd'  ,'>i4'),       # [days]          Truncated Julian Day
        ('burst_sod'  ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('burst_ra'   ,'>i4'),       # [0.0001-deg]    (int)(0.0 to 359.9999 *10000)
        ('burst_dec'  ,'>i4'),       # [0.0001-deg]    (int)(-90.0 to +90.0 *10000)
        ('spare0'     ,'(1,2)>i4'),  # integers        8 bytes for the future
        ('burst_error','>i4'),       # [0.0001-deg]    (int)(0.0 to 180.0 *10000)
        ('phi'        ,'>i4'),       # [centi-deg]     (int)(0.0 to 359.9999 *100)
        ('theta'      ,'>i4'),       # [centi-deg]     (int)(0.0 to +100.0 *100)
        ('spare1'     ,'(1,4)>i4'),  # integer         16 bytes for the future
        ('soln_status','>i4'),       # bits            Type of source/trigger found
        ('misc'       ,'>i4'),       # bits            Misc stuff packed in here
        ('spare2'     ,'(1,2)>i4'),  # integer         8 bytes for the future
        ('loc_algor'  ,'>i4'),       # integer         Location algorithm (1-???)
        ('spare3'     ,'(1,8)>i4'),  # integers        32 bytes for the future
        ('lc_yymmdd'  ,'>i4'),       # integer         The YYMMDD for the lc_url
        ('lc_fff'     ,'>i4'),       # integer         The FFF fraction-of-day for the lc_url
        ('spare4'      ,'(1,6)>i4'), # integer         24 bytes for the future
        ('pkt_term'   ,'>i4')        # integer         Pkt Termination (always = \n)
    ])

# (TYPE=128)
dt_FERMI_LAT_OFFLINE = np.dtype([
        ('pkt_type'   ,'>i4'),       # integer         Packet type number (=128)
        ('pkt_sernum' ,'>i4'),       # integer         1 thru infinity
        ('pkt_hop_cnt','>i4'),       # integer         Incremented by each node
        ('pkt_sod'    ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('trig_num'   ,'>i4'),       # integer         Trigger number
        ('trig_tjd'   ,'>i4'),       # [days]          Truncated Julian Day
        ('trig_sod'   ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('burst_ra'   ,'>i4'),       # [0.0001-deg]    (int)(0.0 to 359.9999 *10000)
        ('burst_dec'  ,'>i4'),       # [0.0001-deg]    (int)(-90.0 to +90.0 *10000)
        ('spare0'     ,'(1,2)>i4'),  # integer         8 bytes for the future
        ('burst_error','>i4'),       # [0.0001-deg]    (int)(0.0 to 180.0 *10000)
        ('spare1'     ,'(1,6)>i4'),  # integer         24 bytes for the future
        ('Trig_ID'    ,'>i4'),       # bits            LAT burst candidate, 1=yes,0=no
        ('misc'       ,'>i4'),       # bits            Misc stuff packed in here
        ('spare'      ,'(1,19)>i4'), # integer         76 bytes for the future
        ('pkt_term'   ,'>i4')        # integer         Pkt Termination (always = \n)
    ])

# (TYPE=149)
dt_SNEWS = np.dtype([
        ('pkt_type'   ,  '>i4'), # integer         Packet type number (=149)
        ('pkt_sernum' ,  '>i4'), # integer         1 thru infinity
        ('pkt_hop_cnt',  '>i4'), # integer         Incremented by each node
        ('pkt_sod'    ,  '>i4'), # [centi-sec]     (int)(sssss.sss *100)
        ('trig_num'   ,  '>i4'), # integer         Trigger num
        ('event_tjd'  ,  '>i4'), # [days]          Truncated Julian Day
        ('event_sod'  ,  '>i4'), # [centi-sec]     (int)(sssss.sss *100)
        ('event_ra'   ,  '>i4'), # [0.0001-deg]    (int)(0.0 to 359.9999 *10000)
        ('event_dec'  ,  '>i4'), # [0.0001-deg]    (int)(-90.0 to +90.0 *10000)
        ('event_flue' ,  '>i4'), # [counts]        Number of neutrinos (0 to infinity)
        ('spare0'     ,  '>i4'), # integer         4 bytes for the future
        ('event_error',  '>i4'), # [0.0001-deg]    (int)(0.0 to 180.0 *10000)
        ('containment',  '>i4'), # [centi-%]       (int)(0.00 to 100.00 *100)
        ('duration'   ,  '>i4'), # [centi-sec]     (int)(0.0 to inf *100)
        ('spare1'     , '4>i4'), # integer         16 bytes for the future
        ('trig_id'    ,  '>i4'), # bits            Trigger identification flags
        ('misc'       ,  '>i4'), # bits            Misc stuff packed in here
        ('spare2'     ,'19>i4'), # integer         76 bytes for the future
        ('pkt_term'   ,  '>i4')  # integer         Pkt Termination (always = \n)
    ])

# (TYPE=151)
dt_LVC_INITIAL = np.dtype([
        ('pkt_type'      ,'>i4'),       # integer         Packet type number (=164)
        ('pkt_sernum'    ,'>i4'),       # integer         1 thru infinity
        ('pkt_hop_cnt'   ,'>i4'),       # integer         Incremented by each node
        ('pkt_sod'       ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('id_num'        ,'>i4'),       # integer         Identification num
        ('event_tjd'     ,'>i4'),       # [days]          Truncated Julian Day
        ('event_sod'     ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('spare0'        ,'(1,2)>i4'),  # integer         8 bytes for the future
        ('fluence'       ,'>i4'),       # [J/m2]]         (int)(log10(fluence)*10000)
        ('peak_freq'     ,'>i4'),       # [centi-Hz]      (int)(Hz*100.0)
        ('FAR'           ,'>i4'),       # [Hz]            (int)(log10(FAR)*10000)
        ('event_type'    ,'>i4'),       # bit_fields      Search/Pipeline/Group index values
        ('trig_subsec'   ,'>i4'),       # [micro-sec]     (int)(0 to 999999)
        ('duration'      ,'>i4'),       # [centi-sec]     (int)(0 to NNN.NN *100)
        ('spare1'        ,'(1,3)>i4'),  # integer         12 bytes for the future
        ('trig_id'       ,'>i4'),       # bits            Trigger identification flags
        ('misc'          ,'>i4'),       # bits            Misc stuff packed in here
        ('ProbNS_Rem'    ,'>i4'),       # bits            (ProbNS*100)*2^16)+(ProbRemnant*100)
        ('MassGap_Let'   ,'>i4'),       # bits            (MassGap*100)*2^24)+(2nd_opt_suffixLetter)
        ('ClassProb'     ,'>i4'),       # 4 bytes         Prob BNS,NSBH,BBH,Terrestrial (*100 each)
        ('ProbInvalFlags','>i4'),       # bits            Flags indicating which probabilities are invalid
        ('spare2'        ,'(1,5)>i4'),  # integer         20 bytes for the future
        ('url_1'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_2'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_3'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_4'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_5'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_6'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_7'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_8'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_9'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_10'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('pkt_term'      ,'>i4')        # integer         Pkt Termination (always = \n)
    ])

# (TYPE=152)
dt_LVC_UPDATE = np.dtype([
        ('pkt_type'      ,'>i4'),       # integer         Packet type number (=164)
        ('pkt_sernum'    ,'>i4'),       # integer         1 thru infinity
        ('pkt_hop_cnt'   ,'>i4'),       # integer         Incremented by each node
        ('pkt_sod'       ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('id_num'        ,'>i4'),       # integer         Identification num
        ('event_tjd'     ,'>i4'),       # [days]          Truncated Julian Day
        ('event_sod'     ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('spare0'        ,'(1,2)>i4'),  # integer         8 bytes for the future
        ('fluence'       ,'>i4'),       # [J/m2]]         (int)(log10(fluence)*10000)
        ('peak_freq'     ,'>i4'),       # [centi-Hz]      (int)(Hz*100.0)
        ('FAR'           ,'>i4'),       # [Hz]            (int)(log10(FAR)*10000)
        ('event_type'    ,'>i4'),       # bit_fields      Search/Pipeline/Group index values
        ('trig_subsec'   ,'>i4'),       # [micro-sec]     (int)(0 to 999999)
        ('duration'      ,'>i4'),       # [centi-sec]     (int)(0 to NNN.NN *100)
        ('spare1'        ,'(1,3)>i4'),  # integer         12 bytes for the future
        ('trig_id'       ,'>i4'),       # bits            Trigger identification flags
        ('misc'          ,'>i4'),       # bits            Misc stuff packed in here
        ('ProbNS_Rem'    ,'>i4'),       # bits            (ProbNS*100)*2^16)+(ProbRemnant*100)
        ('MassGap_Let'   ,'>i4'),       # bits            (MassGap*100)*2^24)+(2nd_opt_suffixLetter)
        ('ClassProb'     ,'>i4'),       # 4 bytes         Prob BNS,NSBH,BBH,Terrestrial (*100 each)
        ('ProbInvalFlags','>i4'),       # bits            Flags indicating which probabilities are invalid
        ('spare2'        ,'(1,5)>i4'),  # integer         20 bytes for the future
        ('url_1'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_2'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_3'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_4'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_5'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_6'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_7'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_8'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_9'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_10'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('pkt_term'      ,'>i4')        # integer         Pkt Termination (always = \n)
    ])

# (TYPE=150)
dt_LVC_PRELIMINARY = np.dtype([
        ('pkt_type'      ,'>i4'),       # integer         Packet type number (=164)
        ('pkt_sernum'    ,'>i4'),       # integer         1 thru infinity
        ('pkt_hop_cnt'   ,'>i4'),       # integer         Incremented by each node
        ('pkt_sod'       ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('id_num'        ,'>i4'),       # integer         Identification num
        ('event_tjd'     ,'>i4'),       # [days]          Truncated Julian Day
        ('event_sod'     ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('spare0'        ,'(1,2)>i4'),  # integer         8 bytes for the future
        ('fluence'       ,'>i4'),       # [J/m2]]         (int)(log10(fluence)*10000)
        ('peak_freq'     ,'>i4'),       # [centi-Hz]      (int)(Hz*100.0)
        ('FAR'           ,'>i4'),       # [Hz]            (int)(log10(FAR)*10000)
        ('event_type'    ,'>i4'),       # bit_fields      Search/Pipeline/Group index values
        ('trig_subsec'   ,'>i4'),       # [micro-sec]     (int)(0 to 999999)
        ('duration'      ,'>i4'),       # [centi-sec]     (int)(0 to NNN.NN *100)
        ('spare1'        ,'(1,3)>i4'),  # integer         12 bytes for the future
        ('trig_id'       ,'>i4'),       # bits            Trigger identification flags
        ('misc'          ,'>i4'),       # bits            Misc stuff packed in here
        ('ProbNS_Rem'    ,'>i4'),       # bits            (ProbNS*100)*2^16)+(ProbRemnant*100)
        ('MassGap_Let'   ,'>i4'),       # bits            (MassGap*100)*2^24)+(2nd_opt_suffixLetter)
        ('ClassProb'     ,'>i4'),       # 4 bytes         Prob BNS,NSBH,BBH,Terrestrial (*100 each)
        ('ProbInvalFlags','>i4'),       # bits            Flags indicating which probabilities are invalid
        ('spare2'        ,'(1,5)>i4'),  # integer         20 bytes for the future
        ('url_1'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_2'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_3'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_4'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_5'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_6'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_7'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_8'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_9'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('url_10'           ,'>S4'),      # chars           The URL for the skymap (?for a retraction?)
        ('pkt_term'      ,'>i4')        # integer         Pkt Termination (always = \n)
    ])

# (TYPE=154)
dt_LVC_COUNTERPART = np.dtype([
        ('pkt_type'      ,'>i4'),       # integer         Packet type number (=164)
        ('pkt_sernum'    ,'>i4'),       # integer         1 thru infinity
        ('pkt_hop_cnt'   ,'>i4'),       # integer         Incremented by each node
        ('pkt_sod'       ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('ref_num'       ,'>i4'),       # integer         Some reference number (eg trig_num)
        ('burst_tjd'     ,'>i4'),       # [days]          Truncated Julian Day
        ('burst_sod'     ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('cp_ra'         ,'>i4'),       # [10^-4-deg]     (int)(0.0 to 359.9999 *10000)
        ('cp_dec'        ,'>i4'),       # [10^-4-deg]     (int)(-90.0 to +90.0 *10000)
        ('cp_inten'      ,'>i4'),       # [centi-mag]     (int)(mm.mm *100)
        ('inten_err'     ,'>i4'),       # [centi-mag]     (int)(mm.mm *100)
        ('cp_error'      ,'>i4'),       # [10^-4-deg]     (int)(0.0 to 180.0 *10000)
        ('filter'        ,'>i4'),       # integer         Opt_fltr, Radio_freq, Oth_??
        ('seeing'        ,'>i4'),       # [centi-arcsec]  (int)(ss.ss *100)
        ('obs_tjd'       ,'>i4'),       # [days]          Truncated Julian Day
        ('obs_time'      ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('obs_dur'       ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('id_conf'       ,'>i4'),       # [centi-%]       (int)(0.0 to 100.00 *100)
        ('flags'         ,'>i4'),       # bits            Flag bits on source-type & ID suffix letters
        ('misc'          ,'>i4'),       # bits            Misc flag bits and fields
        ('telescope'     ,'4>U'),       # chars           The name of the telescope
        ('name'          ,'15>U'),      # chars           The name of the submittor
        ('pkt_term'      ,'>i4')        # integer         Pkt Termination (always = \n)
    ])

# (TYPE=164)
dt_LVC_RETRACTION = np.dtype([
        ('pkt_type'   ,'>i4'),       # integer         Packet type number (=164)
        ('pkt_sernum' ,'>i4'),       # integer         1 thru infinity
        ('pkt_hop_cnt','>i4'),       # integer         Incremented by each node
        ('pkt_sod'    ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('trig_num'   ,'>i4'),       # integer         Trigger num
        ('event_tjd'  ,'>i4'),       # [days]          Truncated Julian Day
        ('event_sod'  ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('spare0'     ,'(1,6)>i4'),  # integer         6 bytes for the future
        ('trig_subsec','>i4'),       # [micro-sec]     (int)(0 to 999999)
        ('spare1'     ,'(1,4)>i4'),  # integer         4 bytes for the future
        ('trig_id'    ,'>i4'),       # bits            Trigger identification flags
        ('misc'       ,'>i4'),       # bits            Misc stuff packed in here
        ('spare2'     ,'(1,19)>i4'), # integer         19 bytes for the future
        ('url'        ,'10>U'),     # chars           The URL for the skymap
        ('pkt_term'   ,'>i4')        # integer         Pkt Termination (always = \n)
    ])

# (TYPE=171)
dt_HAWC_BURST_MONITOR = np.dtype([
        ('pkt_type'   ,'>i4'),      # integer         Packet type number (=171)
        ('pkt_sernum' ,'>i4'),      # integer         1 thru infinity
        ('pkt_hop_cnt','>i4'),      # integer         Incremented by each node
        ('pkt_sod'    ,'>i4'),      # [centi-sec]     (int)(sssss.sss *100)
        ('event_num'  ,'>i4'),      # integer         Event Trigger/ID number
        ('event_tjd'  ,'>i4'),      # [days]          Truncated Julian Day
        ('event_sod'  ,'>i4'),      # [centi-sec]     (int)(sssss.sss *100)
        ('event_ra'   ,'>i4'),      # [0.0001-deg]    (int)(0.0 to 359.9999 *10000)
        ('event_dec'  ,'>i4'),      # [0.0001-deg]    (int)(-90.0 to +90.0 *10000)
        ('spare0'     ,'(1,2)>i4'), # integer         8 bytes for the future
        ('evt_error'  ,'>i4'),      # [0.0001-deg]    (int)(0.0 to 180.0 *10000) 68% Conf
        ('FAR'        ,'>i4'),      # [# per yr]      pow(10.0,slot[12]/10000.0)
        ('deltaT'     ,'>i4'),      # [centi-sec]     (int)(0.0 to NNNN.NN sec *100)
        ('spare1'     ,'>i4'),      # integer         4 bytes for the future
        ('event_ID'   ,'>i4'),      # integer         Event Triger/ID number
        ('stream'     ,'>i4'),      # integer         Which instrument/data source
        ('rev'        ,'>i4'),      # [dn]            0-N (revision/update serial number)
        ('trig_id'    ,'>i4'),      # bits            Trigger identification flags
        ('misc'       ,'>i4'),      # bits            Misc stuff packed in here
        ('pvalue'     ,'>i4'),      # [0.0-1.0]       Probability that is real astrophysical
        ('spare2'     ,'(1,2)>i4'), # integer         16 bytes for the future
        ('run_ID'     ,'>i4'),      # [dn]            Run number in which the Event was found
        ('spare3'     ,'(1,5)>i4'), # integer         20 bytes for the future
        ('url'        ,'10>U'),     # chars           The URL for the skymap
        ('pkt_term'   ,'>i4')       # integer         Pkt Termination (always = \n)
    ])

# (TYPE=172)
dt_AMON_NU_EM_COINC = np.dtype([
        ('pkt_type'   ,'>i4'),      # integer         Packet type number (=171)
        ('pkt_sernum' ,'>i4'),      # integer         1 thru infinity
        ('pkt_hop_cnt','>i4'),      # integer         Incremented by each node
        ('pkt_sod'    ,'>i4'),      # [centi-sec]     (int)(sssss.sss *100)
        ('event_num'  ,'>i4'),      # integer         Event Trigger/ID number
        ('event_tjd'  ,'>i4'),      # [days]          Truncated Julian Day
        ('event_sod'  ,'>i4'),      # [centi-sec]     (int)(sssss.sss *100)
        ('event_ra'   ,'>i4'),      # [0.0001-deg]    (int)(0.0 to 359.9999 *10000)
        ('event_dec'  ,'>i4'),      # [0.0001-deg]    (int)(-90.0 to +90.0 *10000)
        ('n_events'   ,'>i4'),      # integer         CONFIRM THIS
        ('spare0'     ,'>i4'),      # integer         4 bytes for the future
        ('evt_error90','>i4'),      # [0.0001-deg]    (int)(0.0 to 180.0 *10000) 90% Conf
        ('FAR'        ,'>i4'),      # [# per yr]      pow(10.0,slot[12]/10000.0)
        ('deltaT'     ,'>i4'),      # [centi-sec]     (int)(0.0 to 0.999999 *100)
        ('spare1'     ,'(1,2)>i4'), # integer         8 bytes for the future
        ('stream'     ,'>i4'),      # integer         Which instrument/data source
        ('rev'        ,'>i4'),      # [dn]            0-N (revision/update serial number)
        ('trig_id'    ,'>i4'),      # bits            Trigger identification flags
        ('misc'       ,'>i4'),      # bits            Misc stuff packed in here
        ('pvalue'     ,'>i4'),      # [0.0-1.0]       Probability that is real astrophysical  // NOT USED
        ('spare2'     ,'(1,2)>i4'), # integer         8 bytes for the future
        ('run_num'    ,'>i4'),      # [dn]            Run number in which the Event was found
        ('evt_error50','>i4'),      # [0.0001-deg]    (int)(0.0 to 180.0 *10000) 50% Conf
        ('sub_sec'    ,'>i4'),      # integer         Subsec portion of the event_sod trigger time
        ('spare3'     ,'(1,10)>i4'),# integer         40 bytes for the future
        ('url'        ,'3>U'),      # chars           The Event_Date Name for this event
        ('pkt_term'   ,'>i4')       # integer         Pkt Termination (always = \n) 
    ])

# (TYPE=173)
dt_ICECUBE_ASTROTRACK_GOLD = np.dtype([
        ('pkt_type'   ,'>i4'),       # integer         Packet type number (=173)
        ('pkt_sernum' ,'>i4'),       # integer         1 thru infinity
        ('pkt_hop_cnt','>i4'),       # integer         Incremented by each node
        ('pkt_sod'    ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('event_num'  ,'>i4'),       # integer         Event Trigger/ID number
        ('event_tjd'  ,'>i4'),       # [days]          Truncated Julian Day
        ('event_sod'  ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('event_ra'   ,'>i4'),       # [0.0001-deg]    (int)(0.0 to 359.9999 *10000)
        ('event_dec'  ,'>i4'),       # [0.0001-deg]    (int)(-90.0 to +90.0 *10000)
        ('spare0'     ,'(1,2)>i4'),  # integer         8 bytes for the future
        ('evt_error90','>i4'),       # [0.0001-deg]    (int)(0.0 to 180.0 *10000) 90% Conf
        ('event_ID'   ,'>i4'),       # integer         Event Triger/ID number
        ('spare1'     ,'(1,2)>i4'),  # integer         8 bytes for the future
        ('energy'     ,'>i4'),       # TeV             Energy of the neutrino
        ('stream'     ,'>i4'),       # integer         Which instrument/data source
        ('rev'        ,'>i4'),       # [dn]            0-N (revision/update serial number)
        ('trig_id'    ,'>i4'),       # bits            Trigger identification flags
        ('misc'       ,'>i4'),       # bits            Misc stuff packed in here
        ('FAR'        ,'>i4'),       # [N/yr]          False Alerm Rate [N/yr]
        ('spare2'     ,'>i4'),       # integer         4 bytes for the future
        ('signalness' ,'>i4'),       # [0.01-1.0]      (int)(log10(signalness)*10000)
        ('run_ID'     ,'>i4'),       # [dn]            Run number in which the Event was found
        ('evt_error50','>i4'),       # [0.0001-deg]    (int)(0.0 to 180.0 *10000) 50% Conf
        ('spare3'     ,'(1,14)>i4'), # integer         64 bytes for the future
        ('pkt_term'   ,'>i4')        # integer         Pkt Termination (always = \n)
    ])

# (TYPE=174)
dt_ICECUBE_ASTROTRACK_BRONZE = np.dtype([
        ('pkt_type'   ,'>i4'),       # integer         Packet type number (=174)
        ('pkt_sernum' ,'>i4'),       # integer         1 thru infinity
        ('pkt_hop_cnt','>i4'),       # integer         Incremented by each node
        ('pkt_sod'    ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('event_num'  ,'>i4'),       # integer         Event Trigger/ID number
        ('event_tjd'  ,'>i4'),       # [days]          Truncated Julian Day
        ('event_sod'  ,'>i4'),       # [centi-sec]     (int)(sssss.sss *100)
        ('event_ra'   ,'>i4'),       # [0.0001-deg]    (int)(0.0 to 359.9999 *10000)
        ('event_dec'  ,'>i4'),       # [0.0001-deg]    (int)(-90.0 to +90.0 *10000)
        ('spare0'     ,'(1,2)>i4'),  # integer         8 bytes for the future
        ('evt_error90','>i4'),       # [0.0001-deg]    (int)(0.0 to 180.0 *10000) 90% Conf
        ('event_ID'   ,'>i4'),       # integer         Event Triger/ID number
        ('spare1'     ,'(1,2)>i4'),  # integer         8 bytes for the future
        ('energy'     ,'>i4'),       # TeV             Energy of the neutrino
        ('stream'     ,'>i4'),       # integer         Which instrument/data source
        ('rev'        ,'>i4'),       # [dn]            0-N (revision/update serial number)
        ('trig_id'    ,'>i4'),       # bits            Trigger identification flags
        ('misc'       ,'>i4'),       # bits            Misc stuff packed in here
        ('FAR'        ,'>i4'),       # [N/yr]          False Alarm Rate [N/yr]
        ('spare2'     ,'>i4'),       # integer         4 bytes for the future
        ('signalness' ,'>i4'),       # [0.01-1.0]      (int)(log10(signalness)*10000)
        ('run_ID'     ,'>i4'),       # [dn]            Run number in which the Event was found
        ('evt_error50','>i4'),       # [0.0001-deg]    (int)(0.0 to 180.0 *10000) 50% Conf
        ('spare3'     ,'(1,14)>i4'), # integer         56 bytes for the future
        ('pkt_term'   ,'>i4')        # integer         Pkt Termination (always = \n)
    ])

# (TYPE=176)
dt_AMON_ICECUBE_CASCADE = np.dtype([
        ('pkt_type'    ,'>i4'),      # integer         Packet type number (=176)
        ('pkt_sernum'  ,'>i4'),      # integer         1 thru infinity
        ('pkt_hop_cnt' ,'>i4'),      # integer         Incremented by each node
        ('pkt_sod'     ,'>i4'),      # [centi-sec]     (int)(sssss.sss *100)
        ('trig_num'    ,'>i4'),      # integer         Trigger num
        ('event_tjd'   ,'>i4'),      # [days]          Truncated Julian Day
        ('event_sod'   ,'>i4'),      # [centi-sec]     (int)(sssss.sss *100)
        ('ra'          ,'>i4'),      # [0.0001-deg]    (int)(0.0 to 359.9999 *10000)
        ('dec'         ,'>i4'),      # [0.0001-deg]    (int)(-90.0 to +90.0 *10000)
        ('energy'      ,'>i4'),      # [centi-TeV]     (int)(lowest_energy *100)
        ('pos_error_50','>i4'),      # [0.0001-deg]    (int)(0 to 180.0 *10000) 50% Conf
        ('pos_error_90','>i4'),      # [0.0001-deg]    (int)(0 to 180.0 *10000) 90% Conf
        ('far'         ,'>i4'),      # [yr^-1]         (int)(log10(far)*10000)
        ('spare0'      ,'(1,2)>i4'), # integer         8 bytes for the future
        ('event_id'    ,'>i4'),      # integer         AMON Event_ID number
        ('stream'      ,'>i4'),      # integer         AMON Stream number
        ('rev'         ,'>i4'),      # integer         AMON version number
        ('trig_id'     ,'>i4'),      # bits            Trigger identification flags
        ('misc'        ,'>i4'),      # bits            Misc stuff packed in here
        ('spare1'      ,'(1,2)>i4'), # integer         8 bytes for the future
        ('signalness'  ,'>i4'),      # [0.01-1.0]      (int)(log10(signalness)*10000)
        ('run_num'     ,'>i4'),      # integer         AMON Run Number   (in the millions)
        ('spare2'      ,'(1,2)>i4'), # chars           8 bytes for the future
        ('name'        ,'>S12'),     # chars           The common_name string for the event
        ('url'         ,'>S40'),     # chars           The URL for the skywatch_url
        ('pkt_term'    ,'>i4')       # integer         Pkt Termination (always = \n)
    ])




############################################################
###################### UNUSED ALERTS #######################
############################################################
'''
# (TYPE=121) not in KAFKA
def FERMI_LAT_GRB_POS_UPD(value):      
    dt_FERMI_LAT_GRB_POS_UPD =np.dtype([
        ('pkt_type'   ,'>i4'),      # integer         Packet type number (=121)
        ('pkt_sernum' ,'>i4'),      # integer         1 thru infinity
        ('pkt_hop_cnt','>i4'),      # integer         Incremented by each node
        ('pkt_sod'    ,'>i4'),      # [centi-sec]     (int)(sssss.sss *100)
        ('trig_num'   ,'>i4'),      # integer         Trigger number
        ('trig_tjd'   ,'>i4'),      # [days]          Truncated Julian Day
        ('trig_sod'   ,'>i4'),      # [centi-sec]     (int)(sssss.sss *100)
        ('burst_ra'   ,'>i4'),      # [0.0001-deg]    (int)(0.0 to 359.9999 *10000)
        ('burst_dec'  ,'>i4'),      # [0.0001-deg]    (int)(-90.0 to +90.0 *10000)
        ('burst_inten','>i4'),      # [counts]        Num events used in location calc, 0 to inf
        ('inten_4'    ,'>i4'),      # 4_bytes         Evt_cnts in 4 energy bands 
        ('burst_error','>i4'),      # [0.0001-deg]    (int)(0.0 to 180.0 *10000)
        ('phi'        ,'>i4'),      # [centi-deg]     (int)(0.0 to 359.9999 *100)
        ('theta'      ,'>i4'),      # [centi-deg]     (int)(0.0 to +100.0 *100)
        ('int_time'   ,'>i4'),      # [msec]          Integration time
        ('spare0'     ,'(1,2)>i4'), # integer         8 bytes for the future
        ('trig_index' ,'>i4'),      # integer         Trigger index
        ('trig_id'    ,'>i4'),      # bits            LAT burst candidate, 1=yes,0=no
        ('misc'       ,'>i4'),      # bits            Misc stuff packed in here
        ('rec_seq_num','>i4'),      # integer         SerNum of the messages (1-~40)
        ('spare1'     ,'(1,4)>i4'), # integer         16 bytes for the future
        ('temp_stat'  ,'>i4'),      # integer         (int)(4*(-log10(probability)))
        ('image_stat' ,'>i4'),      # integer         (int)(4*(-log10(probability)))
        ('spare2'     ,'(1,4)>i4'), # integer         16 bytes for the future
        ('1st_ph_tjd' ,'>i4'),      # [days]          First photon used in loc calc
        ('1st_ph_sod' ,'>i4'),      # [centi-sec]     (int)(sssss.sss *100)
        ('last_ph_tjd','>i4'),      # [days]          last photon used in loc calc
        ('last_ph_sod','>i4'),      # [centi-sec]     (int)(sssss.sss *100)
        ('spare3'     ,'(1,2)>i4'), # integer         8 bytes for the future
        ('misc1'       ,'>i4'),      # bits            Misc stuff packed in here
        ('loc_qual'   ,'>i4'),      # [0.0001]        Location quality (0.0 - 1.0)
        ('pkt_term'   ,'>i4')       # integer         Pkt Termination (always = \n)
    ])
    np_data = np.frombuffer(value, dt_FERMI_LAT_GRB_POS_UPD)
    if ((np_data['trig_id'][0]>>30)&1) == 1:
        WriteToLogFile('______Its test FERMI_LAT_GRB_POS_UPD notice')
        return(-1)
    else:
        WriteToLogFile('______Its FERMI_LAT_GRB_POS_UPD notice')
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
                'FERMI_LAT_GRB_POS_UPD']
        return(data)
# (TYPE=125) 
def FERMI_LAT_MONITOR(value):  #+++++
    dt_FERMI_LAT_GRB_POS_UPD =np.dtype([
        ('pkt_type'   ,'>i4'),  # integer         Packet type number (=125)
        ('pkt_sernum' ,'>i4'),  # integer         1 thru infinity
        ('pkt_hop_cnt','>i4'),  # integer         Incremented by each node
        ('pkt_sod'    ,'>i4'),  # [centi-sec]     (int)(sssss.sss *100)
        ('ref_num'    ,'>i4'),  # integer         Trigger number
        ('trig_tjd'   ,'>i4'),  # [days]          Truncated Julian Day
        ('trig_sod'   ,'>i4'),  # [centi-sec]     (int)(sssss.sss *100)
        ('trans_ra'   ,'>i4'),  # [0.0001-deg]    (int)(0.0 to 359.9999 *10000)
        ('trans_dec'  ,'>i4'),  # [0.0001-deg]    (int)(-90.0 to +90.0 *10000)
        ('trans_flux' ,'>i4'),  # [ph/cm*2]       (int)(flux*1e9 ph/cm2/sec)
        ('base_flux'  ,'>i4'),  # [ph/cm*2]       (int)(flux*1e9 ph/cm2/sec)
        ('trans_error','>i4'),  # [0.0001-deg]    (int)(0.0 to 180.0 *10000)
        ('cur_flx_err','>i4'),  # [ph/cm*2]       (int)(flux*1e9 ph/cm2/sec)
        ('bas_flx_err','>i4'),  # [ph/cm*2]       (int)(flux*1e9 ph/cm2/sec)
        ('time_scale' ,'>i4'),  # [integer]       Index: 1=1day, 2=1week
        ('e_band'     ,'>i4'),  # [integer]       e1-e2 [GeV] energy_band
        ('spare0'     ,'2>i4'), # integer         8 bytes for the future
        ('trig_id'    ,'>i4'),  # bits            Trigger identification flags
        ('misc'       ,'>i4'),  # bits            Misc stuff packed in here
        ('spare1'     ,'5>i4'), # integer         20 bytes for the future
        ('signif'     ,'>i4'),  # [centi-sigma]   (int)(100*sigma_signif)
        ('spare2'     ,'6>i4'), # integer         24 bytes for the future
        ('src'        ,'17>U'), # chars           The Source name
        ('pkt_term'   ,'>i4')   # integer         Pkt Termination (always = \n)
    ])
    np_data = np.frombuffer(value, dt_FERMI_LAT_GRB_POS_UPD)
    h = math.floor(np_data['trig_sod'][0]/100/60/60)
    m = math.floor(np_data['trig_sod'][0]/100/60)-(h*60)
    s = math.floor(np_data['trig_sod'][0]/100) - (h*60+m)*60
    date = julian.from_jd((np_data['trig_tjd'][0] + 2440000.5), fmt='jd')
    date = date.replace(hour=h,minute=m,second=s)
    data = [date.strftime('%Y-%m-%d.%H:%M:%S'),
            0,
            np_data['trig_tjd'][0],
            np_data['trig_sod'][0]/100, 
            np_data['trans_ra'][0]/10000, 
            np_data['trans_dec'][0]/10000, 
            np_data['trans_error'][0]/10000, 
            'FERMI_LAT_MONITOR']
    SaveGcnMsg(data)
    return(0)
# (TYPE=127)
def FERMI_LAT_GND(value):      #++++
    dt_FERMI_LAT_GND = np.dtype([
        ('pkt_type'    ,'>i4'),      # integer         Packet type number (=127)
        ('pkt_sernum'  ,'>i4'),      # integer         1 thru infinity
        ('pkt_hop_cnt' ,'>i4'),      # integer         Incremented by each node
        ('pkt_sod'     ,'>i4'),      # [centi-sec]     (int)(sssss.sss *100)
        ('trig_num'    ,'>i4'),      # integer         Trigger number
        ('trig_tjd'    ,'>i4'),      # [days]          Truncated Julian Day
        ('trig_sod'    ,'>i4'),      # [centi-sec]     (int)(sssss.sss *100)
        ('burst_ra'    ,'>i4'),      # [0.0001-deg]    (int)(0.0 to 359.9999 *10000
        ('burst_dec'   ,'>i4'),      # [0.0001-deg]    (int)(-90.0 to +90.0 *10000)
        ('tot_inten'   ,'>i4'),      # integer         Total Intensity
        ('spare'       ,'>i4'),      # integer         4 bytes for the future
        ('burst_error' ,'>i4'),      # [0.0001-deg]    (int)(0.0 to 180.0 *10000)
        ('phi'         ,'>i4'),      # [centi-deg]     (int)(0.0 to 359.9999 *100)
        ('theta'       ,'>i4'),      # [centi-deg]     (int)(0.0 to +100.0 *100)
        ('int_time'    ,'>i4'),      # [msec]          Integration time
        ('spare0'      ,'(1,3)>i4'), # integer         12 bytes for the future
        ('trig_id'     ,'>i4'),      # bits            Trigger identification flags
        ('misc'        ,'>i4'),      # bits            Misc stuff packed in here
        ('spare1'      ,'(1,6)>i4'), # integer         24 bytes for the future
        ('signif'      ,'>i4'),      # integer         (int)(sqrt(TS)*100)
        ('inten2'      ,'>i4'),      # centi-cnts      Evt_cnts in the 0.1-1.0 GeV band
        ('inten3'      ,'>i4'),      # centi-cnts      Evt_cnts in the 1.0-10 GeV band
        ('inten4'      ,'>i4'),      # centi-cnts      Evt_cnts in the 10-inf GeV band
        ('spare2'      ,'(1,9)>i4'), # integer         36 bytes for the future
        ('pkt_term'    ,'>i4')       # integer         Pkt Termination (always = \n)
    ])
    np_data = np.frombuffer(value, dt_FERMI_LAT_GND)
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
            'FERMI_LAT_GND']
    SaveGcnMsg(data)
    return(0)
'''
