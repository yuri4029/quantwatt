import qnexus as qnx
qnx.login()
qnx.devices.get_all().df()

#login after each 30days

cirquit = Circuit(2,2)