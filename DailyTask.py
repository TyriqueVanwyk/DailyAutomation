import webbrowser
try:
  ##You can open any application using the imported module
  webbrowser.open_new('https://outlook.office.com/mail/inbox')
  webbrowser.open_new_tab('https://mail.google.com/mail/u/0/#inbox')
except:
    pring("An error occured!")
