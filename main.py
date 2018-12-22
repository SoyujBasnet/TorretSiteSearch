def opener(kwarg):
    import webbrowser
    with open("sites.txt",'r') as file:
        for site in file.readlines():
            try:
                webbrowser.open_new_tab(site.format(kwarg=kwarg))
            except:
                pass
if __name__=="__main__":
    while 1:
        kwarg=input("Enter the thing to search:")
        print("Opening in your default web browser....")
        opener(kwarg)
        
