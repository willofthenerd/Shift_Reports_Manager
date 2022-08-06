from datetime import datetime

import time
import calendar

class shift_timing:
    
    #static start times i.e. morning swing grave

    m_tmin = time.struct_time(tm_hour=8, tm_min=0, tm_sec=0)
    m_tmout = time.struct_time(tm_hour=16, tm_min=0, tm_sec=0)
    s_tmin = time.struct_time(tm_hour=16, tm_min=0, tm_sec=0)
    s_tmout = time.struct_time(tm_hour=0, tm_min=0, tm_sec=0)
    g_tmin = time.struct_time(tm_hour=0, tm_min=0, tm_sec=0)
    g_tmout = time.struct_time(tm_hour=8, tm_min=0, tm_sec=0)


    def __init__(self):
        self.today = datetime.now()
        self.month = today.strftime('%B')
        self.daycount = today.strftime('%d')
        self.year = today.strftime('%Y')


#today = datetime.now()

#month = today.strftime('%B')
#daycount = today.strftime('%d') 
#year = today.strftime('%Y')



#daycount = int(daycount)

#daycount = daycount + 1

#day = str(daycount)