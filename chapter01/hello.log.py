execve("./hello.py", ["./hello.py"], 0xfffff93690e0 /* 15 vars */) = 0
brk(NULL)                               = 0xaaab0f377000
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff991bb000
faccessat(AT_FDCWD, "/etc/ld.so.preload", R_OK) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=28839, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 28839, PROT_READ, MAP_PRIVATE, 3, 0) = 0xffff991b3000
close(3)                                = 0
openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libm.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0\267\0\1\0\0\0\0\0\0\0\0\0\0\0"..., 832) = 832
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=551064, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 680048, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff990df000
mmap(0xffff990e0000, 614512, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0) = 0xffff990e0000
munmap(0xffff990df000, 4096)            = 0
munmap(0xffff99177000, 57456)           = 0
mprotect(0xffff99166000, 61440, PROT_NONE) = 0
mmap(0xffff99175000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x85000) = 0xffff99175000
close(3)                                = 0
openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libexpat.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0\267\0\1\0\0\0\0\0\0\0\0\0\0\0"..., 832) = 832
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=170072, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 299192, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff99096000
mmap(0xffff990a0000, 233656, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0) = 0xffff990a0000
munmap(0xffff99096000, 40960)           = 0
munmap(0xffff990da000, 20664)           = 0
mprotect(0xffff990c7000, 65536, PROT_NONE) = 0
mmap(0xffff990d7000, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x27000) = 0xffff990d7000
close(3)                                = 0
openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libz.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0\267\0\1\0\0\0\0\0\0\0\0\0\0\0"..., 832) = 832
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=104608, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 233648, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff99066000
mmap(0xffff99070000, 168112, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0) = 0xffff99070000
munmap(0xffff99066000, 40960)           = 0
munmap(0xffff9909a000, 20656)           = 0
mprotect(0xffff99088000, 65536, PROT_NONE) = 0
mmap(0xffff99098000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x18000) = 0xffff99098000
close(3)                                = 0
openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0\267\0\1\0\0\0\340u\2\0\0\0\0\0"..., 832) = 832
newfstatat(3, "", {st_mode=S_IFREG|0755, st_size=1637400, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 1805928, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff98eb7000
mmap(0xffff98ec0000, 1740392, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0) = 0xffff98ec0000
munmap(0xffff98eb7000, 36864)           = 0
munmap(0xffff99069000, 28264)           = 0
mprotect(0xffff99048000, 61440, PROT_NONE) = 0
mmap(0xffff99057000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x187000) = 0xffff99057000
mmap(0xffff9905d000, 48744, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0xffff9905d000
close(3)                                = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff991b1000
set_tid_address(0xffff991b14f0)         = 2134
set_robust_list(0xffff991b1500, 24)     = 0
rseq(0xffff991b1bc0, 0x20, 0, 0xd428bc00) = 0
mprotect(0xffff99057000, 16384, PROT_READ) = 0
mprotect(0xffff99098000, 4096, PROT_READ) = 0
mprotect(0xffff990d7000, 8192, PROT_READ) = 0
mprotect(0xffff99175000, 4096, PROT_READ) = 0
mprotect(0xaaaae8f33000, 28672, PROT_READ) = 0
mprotect(0xffff991c0000, 8192, PROT_READ) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
munmap(0xffff991b3000, 28839)           = 0
getrandom("\x05\x47\xf3\xde\x7b\xc7\x6a\xf2", 8, GRND_NONBLOCK) = 8
brk(NULL)                               = 0xaaab0f377000
brk(0xaaab0f398000)                     = 0xaaab0f398000
openat(AT_FDCWD, "/usr/lib/locale/locale-archive", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/share/locale/locale.alias", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/locale/C.UTF-8/LC_CTYPE", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/locale/C.utf8/LC_CTYPE", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=353616, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 353616, PROT_READ, MAP_PRIVATE, 3, 0) = 0xffff98e69000
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/aarch64-linux-gnu/gconv/gconv-modules.cache", O_RDONLY) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=27004, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 27004, PROT_READ, MAP_SHARED, 3, 0) = 0xffff991b4000
close(3)                                = 0
futex(0xffff9905c89c, FUTEX_WAKE_PRIVATE, 2147483647) = 0
getcwd("/usr/src", 4096)                = 9
getrandom("\xf7\x38\x4d\x65\x8d\xb5\x2b\xc2\x9a\xc3\xd9\x89\xc6\x4f\xf3\xb8\x2a\x22\xfd\x78\x12\xb5\x38\x80", 24, GRND_NONBLOCK) = 24
mmap(NULL, 1048576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff98d69000
mmap(NULL, 266240, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff98d28000
mmap(NULL, 135168, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff98d07000
brk(0xaaab0f3bb000)                     = 0xaaab0f3bb000
readlinkat(AT_FDCWD, "/usr/bin/python3", "python3.10", 4096) = 10
readlinkat(AT_FDCWD, "/usr/bin/python3.10", 0xfffff9ae5290, 4096) = -1 EINVAL (Invalid argument)
openat(AT_FDCWD, "/usr/bin/pyvenv.cfg", O_RDONLY) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/pyvenv.cfg", O_RDONLY) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/bin/Modules/Setup.local", 0xfffff9ae6260, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/bin/lib/python3.10/os.py", 0xfffff9ae6150, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/bin/lib/python3.10/os.pyc", 0xfffff9ae6150, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/lib/python3.10/os.py", {st_mode=S_IFREG|0644, st_size=39557, ...}, 0) = 0
openat(AT_FDCWD, "/usr/bin/pybuilddir.txt", O_RDONLY) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/bin/lib/python3.10/lib-dynload", 0xfffff9ae52e0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/lib/python3.10/lib-dynload", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
brk(0xaaab0f3dc000)                     = 0xaaab0f3dc000
mmap(NULL, 1048576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff98c07000
sysinfo({uptime=372314, loads=[19392, 19872, 14720], totalram=6227804160, freeram=324231168, sharedram=326647808, bufferram=415862784, totalswap=1073737728, freeswap=1064751104, procs=724, totalhigh=0, freehigh=0, mem_unit=1}) = 0
openat(AT_FDCWD, "/etc/localtime", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=309, ...}, AT_EMPTY_PATH) = 0
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=309, ...}, AT_EMPTY_PATH) = 0
read(3, "TZif2\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\4\0\0\0\4\0\0\0\0"..., 4096) = 309
lseek(3, -176, SEEK_CUR)                = 133
read(3, "TZif2\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\4\0\0\0\4\0\0\0\0"..., 4096) = 176
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python310.zip", 0xfffff9ae8ac0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/lib", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python310.zip", 0xfffff9ae8850, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
newfstatat(3, "", {st_mode=S_IFDIR|0755, st_size=12288, ...}, AT_EMPTY_PATH) = 0
brk(0xaaab0f404000)                     = 0xaaab0f404000
getdents64(3, 0xaaab0f3db910 /* 207 entries */, 32768) = 6936
getdents64(3, 0xaaab0f3db910 /* 0 entries */, 32768) = 0
close(3)                                = 0
brk(0xaaab0f3ff000)                     = 0xaaab0f3ff000
newfstatat(AT_FDCWD, "/usr/lib/python3.10/encodings/__init__.cpython-310-aarch64-linux-gnu.so", 0xfffff9ae8c70, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/lib/python3.10/encodings/__init__.abi3.so", 0xfffff9ae8c70, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/lib/python3.10/encodings/__init__.so", 0xfffff9ae8c70, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/lib/python3.10/encodings/__init__.py", {st_mode=S_IFREG|0644, st_size=5620, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/encodings/__init__.py", {st_mode=S_IFREG|0644, st_size=5620, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/encodings/__pycache__/__init__.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 3
fcntl(3, F_GETFD)                       = 0x1 (flags FD_CLOEXEC)
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=3875, ...}, AT_EMPTY_PATH) = 0
ioctl(3, TCGETS, 0xfffff9ae8e50)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=3875, ...}, AT_EMPTY_PATH) = 0
read(3, "o\r\r\n\0\0\0\0\275\266\375e\364\25\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 3876) = 3875
read(3, "", 1)                          = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/codecs.py", {st_mode=S_IFREG|0644, st_size=36714, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/codecs.py", {st_mode=S_IFREG|0644, st_size=36714, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/__pycache__/codecs.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=33219, ...}, AT_EMPTY_PATH) = 0
ioctl(3, TCGETS, 0xfffff9ae7fa0)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=33219, ...}, AT_EMPTY_PATH) = 0
read(3, "o\r\r\n\0\0\0\0\275\266\375ej\217\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 33220) = 33219
read(3, "", 1)                          = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/encodings", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/encodings", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/encodings", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/encodings", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
newfstatat(3, "", {st_mode=S_IFDIR|0755, st_size=4096, ...}, AT_EMPTY_PATH) = 0
getdents64(3, 0xaaab0f3ea3b0 /* 125 entries */, 32768) = 4224
getdents64(3, 0xaaab0f3ea3b0 /* 0 entries */, 32768) = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/encodings/aliases.py", {st_mode=S_IFREG|0644, st_size=15677, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/encodings/aliases.py", {st_mode=S_IFREG|0644, st_size=15677, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/encodings/__pycache__/aliases.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=10921, ...}, AT_EMPTY_PATH) = 0
ioctl(3, TCGETS, 0xfffff9ae7890)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=10921, ...}, AT_EMPTY_PATH) = 0
read(3, "o\r\r\n\0\0\0\0\275\266\375e==\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 10922) = 10921
read(3, "", 1)                          = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/encodings", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/encodings/utf_8.py", {st_mode=S_IFREG|0644, st_size=1005, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/encodings/utf_8.py", {st_mode=S_IFREG|0644, st_size=1005, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/encodings/__pycache__/utf_8.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=1597, ...}, AT_EMPTY_PATH) = 0
ioctl(3, TCGETS, 0xfffff9ae8ed0)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=1597, ...}, AT_EMPTY_PATH) = 0
read(3, "o\r\r\n\0\0\0\0\275\266\375e\355\3\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 1598) = 1597
read(3, "", 1)                          = 0
close(3)                                = 0
rt_sigaction(SIGPIPE, {sa_handler=SIG_IGN, sa_mask=[], sa_flags=SA_ONSTACK}, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGXFSZ, {sa_handler=SIG_IGN, sa_mask=[], sa_flags=SA_ONSTACK}, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGHUP, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGINT, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGQUIT, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGILL, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGTRAP, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGABRT, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGBUS, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGFPE, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGKILL, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGUSR1, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGSEGV, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGUSR2, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGPIPE, NULL, {sa_handler=SIG_IGN, sa_mask=[], sa_flags=SA_ONSTACK}, 8) = 0
rt_sigaction(SIGALRM, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGTERM, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGSTKFLT, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGCHLD, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGCONT, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGSTOP, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGTSTP, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGTTIN, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGTTOU, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGURG, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGXCPU, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGXFSZ, NULL, {sa_handler=SIG_IGN, sa_mask=[], sa_flags=SA_ONSTACK}, 8) = 0
rt_sigaction(SIGVTALRM, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGPROF, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGWINCH, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGIO, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGPWR, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGSYS, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_2, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_3, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_4, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_5, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_6, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_7, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_8, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_9, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_10, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_11, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_12, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_13, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_14, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_15, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_16, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_17, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_18, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_19, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_20, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_21, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_22, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_23, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_24, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_25, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_26, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_27, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_28, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_29, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_30, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_31, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGRT_32, NULL, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGINT, {sa_handler=0xaaaae8c4de20, sa_mask=[], sa_flags=SA_ONSTACK}, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
newfstatat(0, "", {st_mode=S_IFCHR|0600, st_rdev=makedev(0x88, 0x2), ...}, AT_EMPTY_PATH) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/io.py", {st_mode=S_IFREG|0644, st_size=4196, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/io.py", {st_mode=S_IFREG|0644, st_size=4196, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/__pycache__/io.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=3663, ...}, AT_EMPTY_PATH) = 0
ioctl(3, TCGETS, 0xfffff9ae8f50)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=3663, ...}, AT_EMPTY_PATH) = 0
read(3, "o\r\r\n\0\0\0\0\275\266\375ed\20\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 3664) = 3663
read(3, "", 1)                          = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/abc.py", {st_mode=S_IFREG|0644, st_size=6522, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/abc.py", {st_mode=S_IFREG|0644, st_size=6522, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/__pycache__/abc.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=6751, ...}, AT_EMPTY_PATH) = 0
ioctl(3, TCGETS, 0xfffff9ae80a0)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=6751, ...}, AT_EMPTY_PATH) = 0
read(3, "o\r\r\n\0\0\0\0\275\266\375ez\31\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 6752) = 6751
read(3, "", 1)                          = 0
close(3)                                = 0
dup(0)                                  = 3
close(3)                                = 0
newfstatat(0, "", {st_mode=S_IFCHR|0600, st_rdev=makedev(0x88, 0x2), ...}, AT_EMPTY_PATH) = 0
ioctl(0, TCGETS, {B38400 opost isig icanon echo ...}) = 0
lseek(0, 0, SEEK_CUR)                   = -1 ESPIPE (Illegal seek)
ioctl(0, TCGETS, {B38400 opost isig icanon echo ...}) = 0
dup(1)                                  = 3
close(3)                                = 0
newfstatat(1, "", {st_mode=S_IFCHR|0600, st_rdev=makedev(0x88, 0x2), ...}, AT_EMPTY_PATH) = 0
ioctl(1, TCGETS, {B38400 opost isig icanon echo ...}) = 0
lseek(1, 0, SEEK_CUR)                   = -1 ESPIPE (Illegal seek)
ioctl(1, TCGETS, {B38400 opost isig icanon echo ...}) = 0
dup(2)                                  = 3
close(3)                                = 0
newfstatat(2, "", {st_mode=S_IFCHR|0600, st_rdev=makedev(0x88, 0x2), ...}, AT_EMPTY_PATH) = 0
ioctl(2, TCGETS, {B38400 opost isig icanon echo ...}) = 0
lseek(2, 0, SEEK_CUR)                   = -1 ESPIPE (Illegal seek)
ioctl(2, TCGETS, {B38400 opost isig icanon echo ...}) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/site.py", {st_mode=S_IFREG|0644, st_size=23667, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/site.py", {st_mode=S_IFREG|0644, st_size=23667, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/__pycache__/site.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=17922, ...}, AT_EMPTY_PATH) = 0
ioctl(3, TCGETS, 0xfffff9ae8f50)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=17922, ...}, AT_EMPTY_PATH) = 0
read(3, "o\r\r\n\0\0\0\0\275\266\375es\\\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 17923) = 17922
read(3, "", 1)                          = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/os.py", {st_mode=S_IFREG|0644, st_size=39557, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/os.py", {st_mode=S_IFREG|0644, st_size=39557, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/__pycache__/os.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=31599, ...}, AT_EMPTY_PATH) = 0
ioctl(3, TCGETS, 0xfffff9ae80a0)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=31599, ...}, AT_EMPTY_PATH) = 0
read(3, "o\r\r\n\0\0\0\0\275\266\375e\205\232\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 31600) = 31599
read(3, "", 1)                          = 0
close(3)                                = 0
brk(0xaaab0f420000)                     = 0xaaab0f420000
mmap(NULL, 151552, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff98be2000
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/stat.py", {st_mode=S_IFREG|0644, st_size=5485, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/stat.py", {st_mode=S_IFREG|0644, st_size=5485, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/__pycache__/stat.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=4273, ...}, AT_EMPTY_PATH) = 0
ioctl(3, TCGETS, 0xfffff9ae71f0)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=4273, ...}, AT_EMPTY_PATH) = 0
read(3, "o\r\r\n\0\0\0\0\275\266\375em\25\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 4274) = 4273
read(3, "", 1)                          = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/_collections_abc.py", {st_mode=S_IFREG|0644, st_size=32284, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/_collections_abc.py", {st_mode=S_IFREG|0644, st_size=32284, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/__pycache__/_collections_abc.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=32925, ...}, AT_EMPTY_PATH) = 0
ioctl(3, TCGETS, 0xfffff9ae71f0)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=32925, ...}, AT_EMPTY_PATH) = 0
read(3, "o\r\r\n\0\0\0\0\275\266\375e\34~\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 32926) = 32925
read(3, "", 1)                          = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/posixpath.py", {st_mode=S_IFREG|0644, st_size=16250, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/posixpath.py", {st_mode=S_IFREG|0644, st_size=16250, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/__pycache__/posixpath.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=10530, ...}, AT_EMPTY_PATH) = 0
ioctl(3, TCGETS, 0xfffff9ae71f0)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=10530, ...}, AT_EMPTY_PATH) = 0
read(3, "o\r\r\n\0\0\0\0\275\266\375ez?\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 10531) = 10530
read(3, "", 1)                          = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/genericpath.py", {st_mode=S_IFREG|0644, st_size=4975, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/genericpath.py", {st_mode=S_IFREG|0644, st_size=4975, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/__pycache__/genericpath.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=3907, ...}, AT_EMPTY_PATH) = 0
ioctl(3, TCGETS, 0xfffff9ae6340)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=3907, ...}, AT_EMPTY_PATH) = 0
read(3, "o\r\r\n\0\0\0\0\275\266\375eo\23\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 3908) = 3907
read(3, "", 1)                          = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/_sitebuiltins.py", {st_mode=S_IFREG|0644, st_size=3128, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/_sitebuiltins.py", {st_mode=S_IFREG|0644, st_size=3128, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/__pycache__/_sitebuiltins.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=3547, ...}, AT_EMPTY_PATH) = 0
ioctl(3, TCGETS, 0xfffff9ae80a0)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=3547, ...}, AT_EMPTY_PATH) = 0
read(3, "o\r\r\n\0\0\0\0\275\266\375e8\f\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 3548) = 3547
read(3, "", 1)                          = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/bin/pyvenv.cfg", 0xfffff9ae8b60, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/pyvenv.cfg", 0xfffff9ae8b60, 0) = -1 ENOENT (No such file or directory)
geteuid()                               = 0
getuid()                                = 0
getegid()                               = 0
getgid()                                = 0
newfstatat(AT_FDCWD, "/root/.local/lib/python3.10/site-packages", 0xfffff9ae8d40, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/local/lib/python3.10/dist-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.10/dist-packages", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
newfstatat(3, "", {st_mode=S_IFDIR|0755, st_size=4096, ...}, AT_EMPTY_PATH) = 0
getdents64(3, 0xaaab0f401760 /* 2 entries */, 32768) = 48
getdents64(3, 0xaaab0f401760 /* 0 entries */, 32768) = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3/dist-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3/dist-packages", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
newfstatat(3, "", {st_mode=S_IFDIR|0755, st_size=4096, ...}, AT_EMPTY_PATH) = 0
getdents64(3, 0xaaab0f401760 /* 104 entries */, 32768) = 4200
getdents64(3, 0xaaab0f401760 /* 0 entries */, 32768) = 0
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/python3/dist-packages/matplotlib-3.5.1-nspkg.pth", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=569, ...}, AT_EMPTY_PATH) = 0
ioctl(3, TCGETS, 0xfffff9ae86e0)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
ioctl(3, TCGETS, 0xfffff9ae8a70)        = -1 ENOTTY (Inappropriate ioctl for device)
read(3, "import sys, types, os;has_mfs = "..., 8192) = 569
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/types.py", {st_mode=S_IFREG|0644, st_size=10117, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/types.py", {st_mode=S_IFREG|0644, st_size=10117, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/__pycache__/types.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 4
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=9525, ...}, AT_EMPTY_PATH) = 0
ioctl(4, TCGETS, 0xfffff9ae7590)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(4, 0, SEEK_CUR)                   = 0
lseek(4, 0, SEEK_CUR)                   = 0
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=9525, ...}, AT_EMPTY_PATH) = 0
read(4, "o\r\r\n\0\0\0\0\275\266\375e\205'\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 9526) = 9525
read(4, "", 1)                          = 0
close(4)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/importlib/__init__.cpython-310-aarch64-linux-gnu.so", 0xfffff9ae69f0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/lib/python3.10/importlib/__init__.abi3.so", 0xfffff9ae69f0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/lib/python3.10/importlib/__init__.so", 0xfffff9ae69f0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/lib/python3.10/importlib/__init__.py", {st_mode=S_IFREG|0644, st_size=6089, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/importlib/__init__.py", {st_mode=S_IFREG|0644, st_size=6089, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/importlib/__pycache__/__init__.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 4
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=3805, ...}, AT_EMPTY_PATH) = 0
ioctl(4, TCGETS, 0xfffff9ae6bd0)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(4, 0, SEEK_CUR)                   = 0
lseek(4, 0, SEEK_CUR)                   = 0
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=3805, ...}, AT_EMPTY_PATH) = 0
read(4, "o\r\r\n\0\0\0\0\275\266\375e\311\27\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 3806) = 3805
read(4, "", 1)                          = 0
close(4)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/warnings.py", {st_mode=S_IFREG|0644, st_size=19688, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/warnings.py", {st_mode=S_IFREG|0644, st_size=19688, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/__pycache__/warnings.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 4
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=13646, ...}, AT_EMPTY_PATH) = 0
ioctl(4, TCGETS, 0xfffff9ae5d20)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(4, 0, SEEK_CUR)                   = 0
lseek(4, 0, SEEK_CUR)                   = 0
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=13646, ...}, AT_EMPTY_PATH) = 0
read(4, "o\r\r\n\0\0\0\0\275\266\375e\350L\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 13647) = 13646
read(4, "", 1)                          = 0
close(4)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/importlib", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/importlib", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/importlib", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/importlib", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 4
newfstatat(4, "", {st_mode=S_IFDIR|0755, st_size=4096, ...}, AT_EMPTY_PATH) = 0
getdents64(4, 0xaaab0f40b5b0 /* 15 entries */, 32768) = 488
getdents64(4, 0xaaab0f40b5b0 /* 0 entries */, 32768) = 0
close(4)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/importlib/util.py", {st_mode=S_IFREG|0644, st_size=11487, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/importlib/util.py", {st_mode=S_IFREG|0644, st_size=11487, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/importlib/__pycache__/util.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 4
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=9329, ...}, AT_EMPTY_PATH) = 0
ioctl(4, TCGETS, 0xfffff9ae74c0)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(4, 0, SEEK_CUR)                   = 0
lseek(4, 0, SEEK_CUR)                   = 0
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=9329, ...}, AT_EMPTY_PATH) = 0
read(4, "o\r\r\n\0\0\0\0\275\266\375e\337,\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 9330) = 9329
read(4, "", 1)                          = 0
close(4)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/importlib", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/importlib/_abc.py", {st_mode=S_IFREG|0644, st_size=1852, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/importlib/_abc.py", {st_mode=S_IFREG|0644, st_size=1852, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/importlib/__pycache__/_abc.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 4
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=1971, ...}, AT_EMPTY_PATH) = 0
ioctl(4, TCGETS, 0xfffff9ae6610)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(4, 0, SEEK_CUR)                   = 0
lseek(4, 0, SEEK_CUR)                   = 0
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=1971, ...}, AT_EMPTY_PATH) = 0
read(4, "o\r\r\n\0\0\0\0\275\266\375e<\7\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 1972) = 1971
read(4, "", 1)                          = 0
close(4)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/contextlib.py", {st_mode=S_IFREG|0644, st_size=25882, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/contextlib.py", {st_mode=S_IFREG|0644, st_size=25882, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/__pycache__/contextlib.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 4
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=20895, ...}, AT_EMPTY_PATH) = 0
ioctl(4, TCGETS, 0xfffff9ae6610)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(4, 0, SEEK_CUR)                   = 0
lseek(4, 0, SEEK_CUR)                   = 0
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=20895, ...}, AT_EMPTY_PATH) = 0
read(4, "o\r\r\n\0\0\0\0\275\266\375e\32e\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 20896) = 20895
read(4, "", 1)                          = 0
close(4)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/collections/__init__.cpython-310-aarch64-linux-gnu.so", 0xfffff9ae5580, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/lib/python3.10/collections/__init__.abi3.so", 0xfffff9ae5580, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/lib/python3.10/collections/__init__.so", 0xfffff9ae5580, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/lib/python3.10/collections/__init__.py", {st_mode=S_IFREG|0644, st_size=51398, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/collections/__init__.py", {st_mode=S_IFREG|0644, st_size=51398, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/collections/__pycache__/__init__.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 4
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=48453, ...}, AT_EMPTY_PATH) = 0
ioctl(4, TCGETS, 0xfffff9ae5760)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(4, 0, SEEK_CUR)                   = 0
lseek(4, 0, SEEK_CUR)                   = 0
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=48453, ...}, AT_EMPTY_PATH) = 0
read(4, "o\r\r\n\0\0\0\0\275\266\375e\306\310\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 48454) = 48453
read(4, "", 1)                          = 0
close(4)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/keyword.py", {st_mode=S_IFREG|0644, st_size=1061, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/keyword.py", {st_mode=S_IFREG|0644, st_size=1061, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/__pycache__/keyword.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 4
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=927, ...}, AT_EMPTY_PATH) = 0
ioctl(4, TCGETS, 0xfffff9ae48b0)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(4, 0, SEEK_CUR)                   = 0
lseek(4, 0, SEEK_CUR)                   = 0
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=927, ...}, AT_EMPTY_PATH) = 0
read(4, "o\r\r\n\0\0\0\0\275\266\375e%\4\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 928) = 927
read(4, "", 1)                          = 0
close(4)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/operator.py", {st_mode=S_IFREG|0644, st_size=10751, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/operator.py", {st_mode=S_IFREG|0644, st_size=10751, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/__pycache__/operator.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 4
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=13508, ...}, AT_EMPTY_PATH) = 0
ioctl(4, TCGETS, 0xfffff9ae48b0)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(4, 0, SEEK_CUR)                   = 0
lseek(4, 0, SEEK_CUR)                   = 0
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=13508, ...}, AT_EMPTY_PATH) = 0
read(4, "o\r\r\n\0\0\0\0\275\266\375e\377)\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 13509) = 13508
read(4, "", 1)                          = 0
close(4)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/reprlib.py", {st_mode=S_IFREG|0644, st_size=5267, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/reprlib.py", {st_mode=S_IFREG|0644, st_size=5267, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/__pycache__/reprlib.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 4
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=5250, ...}, AT_EMPTY_PATH) = 0
ioctl(4, TCGETS, 0xfffff9ae48b0)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(4, 0, SEEK_CUR)                   = 0
lseek(4, 0, SEEK_CUR)                   = 0
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=5250, ...}, AT_EMPTY_PATH) = 0
read(4, "o\r\r\n\0\0\0\0\275\266\375e\223\24\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 5251) = 5250
read(4, "", 1)                          = 0
close(4)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/functools.py", {st_mode=S_IFREG|0644, st_size=38076, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/functools.py", {st_mode=S_IFREG|0644, st_size=38076, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/__pycache__/functools.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 4
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=28335, ...}, AT_EMPTY_PATH) = 0
ioctl(4, TCGETS, 0xfffff9ae5760)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(4, 0, SEEK_CUR)                   = 0
lseek(4, 0, SEEK_CUR)                   = 0
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=28335, ...}, AT_EMPTY_PATH) = 0
brk(0xaaab0f444000)                     = 0xaaab0f444000
read(4, "o\r\r\n\0\0\0\0\275\266\375e\274\224\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 28336) = 28335
read(4, "", 1)                          = 0
close(4)                                = 0
brk(0xaaab0f43e000)                     = 0xaaab0f43e000
newfstatat(AT_FDCWD, "/usr/lib/python3.10/importlib", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/importlib/machinery.py", {st_mode=S_IFREG|0644, st_size=831, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/importlib/machinery.py", {st_mode=S_IFREG|0644, st_size=831, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/importlib/__pycache__/machinery.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 4
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=944, ...}, AT_EMPTY_PATH) = 0
ioctl(4, TCGETS, 0xfffff9ae74c0)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(4, 0, SEEK_CUR)                   = 0
lseek(4, 0, SEEK_CUR)                   = 0
newfstatat(4, "", {st_mode=S_IFREG|0644, st_size=944, ...}, AT_EMPTY_PATH) = 0
read(4, "o\r\r\n\0\0\0\0\275\266\375e?\3\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 945) = 944
read(4, "", 1)                          = 0
close(4)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3/dist-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3/dist-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3/dist-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3/dist-packages", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 4
newfstatat(4, "", {st_mode=S_IFDIR|0755, st_size=4096, ...}, AT_EMPTY_PATH) = 0
getdents64(4, 0xaaab0f426200 /* 104 entries */, 32768) = 4200
getdents64(4, 0xaaab0f426200 /* 0 entries */, 32768) = 0
close(4)                                = 0
mmap(NULL, 1048576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffff98ae2000
newfstatat(AT_FDCWD, "/usr/lib/python3/dist-packages/mpl_toolkits/__init__.cpython-310-aarch64-linux-gnu.so", 0xfffff9ae7bd0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/lib/python3/dist-packages/mpl_toolkits/__init__.abi3.so", 0xfffff9ae7bd0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/lib/python3/dist-packages/mpl_toolkits/__init__.so", 0xfffff9ae7bd0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/usr/lib/python3/dist-packages/mpl_toolkits/__init__.py", {st_mode=S_IFREG|0644, st_size=122, ...}, 0) = 0
read(3, "", 8192)                       = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/dist-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/dist-packages", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
newfstatat(3, "", {st_mode=S_IFDIR|0755, st_size=4096, ...}, AT_EMPTY_PATH) = 0
getdents64(3, 0xaaab0f401760 /* 3 entries */, 32768) = 80
getdents64(3, 0xaaab0f401760 /* 0 entries */, 32768) = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/sitecustomize.py", {st_mode=S_IFREG|0644, st_size=155, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/sitecustomize.py", {st_mode=S_IFREG|0644, st_size=155, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/__pycache__/sitecustomize.cpython-310.pyc", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=225, ...}, AT_EMPTY_PATH) = 0
ioctl(3, TCGETS, 0xfffff9ae7ce0)        = -1 ENOTTY (Inappropriate ioctl for device)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=225, ...}, AT_EMPTY_PATH) = 0
read(3, "o\r\r\n\0\0\0\0\275\266\375e\233\0\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 226) = 225
read(3, "", 1)                          = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/lib-dynload", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/lib-dynload", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/lib-dynload", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/lib-dynload", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
newfstatat(3, "", {st_mode=S_IFDIR|0755, st_size=4096, ...}, AT_EMPTY_PATH) = 0
getdents64(3, 0xaaab0f401760 /* 49 entries */, 32768) = 3136
getdents64(3, 0xaaab0f401760 /* 0 entries */, 32768) = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.10/dist-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.10/dist-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.10/dist-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/local/lib/python3.10/dist-packages", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
newfstatat(3, "", {st_mode=S_IFDIR|0755, st_size=4096, ...}, AT_EMPTY_PATH) = 0
getdents64(3, 0xaaab0f401760 /* 2 entries */, 32768) = 48
getdents64(3, 0xaaab0f401760 /* 0 entries */, 32768) = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3/dist-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/dist-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/dist-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/dist-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
openat(AT_FDCWD, "/usr/lib/python3.10/dist-packages", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
newfstatat(3, "", {st_mode=S_IFDIR|0755, st_size=4096, ...}, AT_EMPTY_PATH) = 0
getdents64(3, 0xaaab0f401760 /* 3 entries */, 32768) = 80
getdents64(3, 0xaaab0f401760 /* 0 entries */, 32768) = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10", {st_mode=S_IFDIR|0755, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/lib-dynload", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/local/lib/python3.10/dist-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3/dist-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/lib/python3.10/dist-packages", {st_mode=S_IFDIR|0755, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/usr/src/./hello.py", {st_mode=S_IFREG|0755, st_size=42, ...}, 0) = 0
openat(AT_FDCWD, "/usr/src/./hello.py", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0755, st_size=42, ...}, AT_EMPTY_PATH) = 0
ioctl(3, TCGETS, 0xfffff9ae9e20)        = -1 ENOSYS (Function not implemented)
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
lseek(3, -22, SEEK_END)                 = 20
lseek(3, 0, SEEK_CUR)                   = 20
read(3, "rint(\"Hello, World!\")\n", 4096) = 22
lseek(3, 0, SEEK_END)                   = 42
lseek(3, 0, SEEK_CUR)                   = 42
lseek(3, 0, SEEK_SET)                   = 0
lseek(3, 0, SEEK_CUR)                   = 0
newfstatat(3, "", {st_mode=S_IFREG|0755, st_size=42, ...}, AT_EMPTY_PATH) = 0
read(3, "#!/usr/bin/python3\nprint(\"Hello,"..., 43) = 42
read(3, "", 1)                          = 0
lseek(3, 0, SEEK_SET)                   = 0
close(3)                                = 0
newfstatat(AT_FDCWD, "/usr/src/./hello.py", {st_mode=S_IFREG|0755, st_size=42, ...}, 0) = 0
readlinkat(AT_FDCWD, "./hello.py", 0xfffff9ad98c0, 4096) = -1 EINVAL (Invalid argument)
getcwd("/usr/src", 1024)                = 9
readlinkat(AT_FDCWD, "/usr/src/hello.py", 0xfffff9ad9030, 1023) = -1 EINVAL (Invalid argument)
openat(AT_FDCWD, "/usr/src/./hello.py", O_RDONLY) = 3
ioctl(3, FIOCLEX)                       = 0
newfstatat(3, "", {st_mode=S_IFREG|0755, st_size=42, ...}, AT_EMPTY_PATH) = 0
ioctl(3, TCGETS, 0xfffff9aea810)        = -1 ENOSYS (Function not implemented)
lseek(3, 0, SEEK_CUR)                   = 0
newfstatat(3, "", {st_mode=S_IFREG|0755, st_size=42, ...}, AT_EMPTY_PATH) = 0
read(3, "#!/usr/bin/python3\nprint(\"Hello,"..., 4096) = 42
lseek(3, 0, SEEK_SET)                   = 0
read(3, "#!/usr/bin/python3\nprint(\"Hello,"..., 4096) = 42
read(3, "", 4096)                       = 0
close(3)                                = 0
write(1, "Hello, World!\n", 14)         = 14
rt_sigaction(SIGINT, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=SA_ONSTACK}, {sa_handler=0xaaaae8c4de20, sa_mask=[], sa_flags=SA_ONSTACK}, 8) = 0
munmap(0xffff98be2000, 151552)          = 0
exit_group(0)                           = ?
+++ exited with 0 +++
