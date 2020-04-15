def setup():
    import os
    import time
    print("Hello and welcome to BlogTeX.")
    time.sleep(3)
    print("We are setting up the program. One moment please...")

    try:
        import PyInquirer
    except:
        os.system('pip install PyInquirer')
    try:
        import feedparser as fr
    except:
        os.system('pip install feedparser')
    os.system('mkdir files') 
