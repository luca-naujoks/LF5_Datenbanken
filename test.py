"""psw = "Hallo" #Hallo

psw2 = b'$2b$12$ygaAEyqBSk.MeqIlUBLIi.WMH5EnyP0yfnC29OGbzi6cWlYGOgOV2'

pswd = psw.encode("utf-8")

salt =

crypto = bcrypt.hashpw(
    pswd,
    salt
)
if psw == psw2:
    print("yep")
else:
    print("nope")
print(salt)
print(crypto)"""

import bcrypt
usersalt = b'$2b$12$Nj0NOk2xZzRogZOceKql9u'

db = b'$2b$12$pva0/W4DU09xWIWoHvrsgOgWh.mCwfUZWfCCxQuSDJnuJBeHeEPVi'

passwd = b's$cret12'

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(passwd, salt)
print(hashed)
print(salt)
if bcrypt.checkpw(passwd, db):
    print("match")
else:
    print("does not match")




