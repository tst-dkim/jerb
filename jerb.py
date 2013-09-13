import os
import socket

# do something useful that makes me money
print os.uname()
# ip address? hopefully!
print socket.gethostbyname(socket.gethostname())

# uncomment to do nothing useful except return a non-zero error code
#sys.exit(1)
