import yagmail
yagmail.register("rndjsports@gmail.com","rndjsports123")
yag = yagmail.SMTP('rndjsports@gmail.com')
yag.send('sanketyou8@gmail.com', subject = None, contents = 'Hello')