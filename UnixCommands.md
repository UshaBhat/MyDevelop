># Unix Commands

>## 1. adduser
* adduser command in Linux is used to add a new user to your current Linux machine. 

>**$ sudo adduser username**
Adding user `username' ... 
Adding new group `username' (1000) ...
Adding new user `username' (1000) with group `username' ...
Creating home directory `/home/username' ...
Copying files from `/etc/skel' ...
New password:
Retype new password:
passwd: password updated successfully
Changing the user information for username
Enter the new value, or press ENTER for the default

	Full Name []: Usha Bhat
	Room Number []: 12
	Work Phone []: 
	Home Phone []: 
	Other []: Is the information correct? [Y/n] y

>## 2. addgroup
* addgroup command in Linux is used to add a new group to your current Linux machine.

>**$ sudo addgroup groupname**
[sudo] password for ushabhat: 
Adding group `groupname' (GID 1002) ...
Done.

>## 3. cat
* The cat command is a multi-purpose utility in the Linux system. It can be used to create a file, display content of the file, copy the content of one file to another file, and more.

>**cat> Demo.txt**
ushabhat@ushabhat-Latitude-5531:~/Desktop$ cat> Demo.txt
This is a text file
ushabhat@ushabhat-Latitude-5531:~/Desktop$ cat Demo.txt
This is a text file


>## 4. cd
* The cd command is used to change the current directory.

>**cd \<directory name>**

>## 5. chmod
* In Unix-like operating systems, the chmod command is used to change the access mode of a file.
The name is an abbreviation of change mode.

>ushabhat@ushabhat-Latitude-5531:~/Desktop$ chmod o+w *.txt
ushabhat@ushabhat-Latitude-5531:~/Desktop$ ls -l *.txt

-rw-rw-rw- 1 ushabhat ushabhat 20 Feb 28 03:37 Demo.txt

>## 6. chown
*  command is used to change the file Owner or group. Whenever you want to change ownership you can use chown command.

>ushabhat@ushabhat-Latitude-5531:~/Desktop$ sudo chown ushabhat Demo.txt
[sudo] password for ushabhat: 
ushabhat@ushabhat-Latitude-5531:~/Desktop$ ls -l Demo.txt
-rw-rw-rw- 1 ushabhat ushabhat 20 Feb 28 03:37 Demo.txt
ushabhat@ushabhat-Latitude-5531:~/Desktop$ 

>## 7. clear

* clear is a standard Unix computer operating system command that is used to clear the terminal screen

>**$ clear**

>## 8. cp
* 'cp' means copy. 'cp' command is used to copy a file or a directory.

>ushabhat@ushabhat-Latitude-5531:~/Desktop$ ls
Demo.txt
ushabhat@ushabhat-Latitude-5531:~/Desktop$ cp Demo.txt new.txt
ushabhat@ushabhat-Latitude-5531:~/Desktop$ ls
Demo.txt  new.txt
ushabhat@ushabhat-Latitude-5531:~/Desktop$ cat new.txt
This is a text file

>## 9. cut
* Linux cut command is useful for selecting a specific column of a file. It is used to cut a specific sections by byte position, character, and field and writes them to standard output. It cuts a line and extracts the text data. It is necessary to pass an argument with it; otherwise, it will throw an error message.

>ushabhat@ushabhat-Latitude-5531:~/Desktop$ cat> marks.txt
alex-50
java-70
carry-76
ushabhat@ushabhat-Latitude-5531:~/Desktop$ cut -d- -f2 marks.txt
50
70
76

>## 10. date
* It is used to display systems date and current time

>$date
Tuesday 28 February 2023 04:41:52 AM IST

>## 11. deluser 
* userdel command in Linux system is used to delete a user account and related files. 

> ushabhat@ushabhat-Latitude-5531:~/Desktop$ ls /home/
newuser  username  ushabhat
ushabhat@ushabhat-Latitude-5531:~/Desktop$ sudo userdel -r newuser
userdel: user 'newuser' does not exist

>## 12. delgroup
* delgroup command is used to delete usergroup.

> ushabhat@ushabhat-Latitude-5531:~/Desktop$ sudo addgroup username
Adding group `username' (GID 1000) ...
Done.
>
>ushabhat@ushabhat-Latitude-5531:~/Desktop$ sudo delgroup username
Removing group `username' ...
Done.

> ## 13. echo
* Displaying a string on the terminal
To print text or a string on the terminal, use the syntax

> ushabhat@ushabhat-Latitude-5531:~/Desktop$ echo "Welcome to Linux" 
Welcome to Linux

> ## 14. find
* The find command in UNIX is a command line utility for walking a file hierarchy. It can be used to find files and directories and perform subsequent operations on them.
> ushabhat@ushabhat-Latitude-5531:~/Desktop$ find /home/ -name Demo.txt
/home/ushabhat/.local/share/Trash/files/Demo.txt

> ## 15. grep 
* Grep is a useful command to search for matching patterns in a file. grep is short for "global regular expression print".

> ushabhat@ushabhat-Latitude-5531:~/Desktop$ grep "is" Demo.txt
> 
>There is a bird

>## 16. head
* head command is a command-line utility, which prints the first 10 lines of the specified files. If more than one file name is provided then data from each file is preceded by its file name.

> $ head
> 
> ushabhat@ushabhat-Latitude-5531:~/Desktop$ head Demo.txt
123
234
345
456
567
567
678
789
890
901

>## 17. history
* Bash and Korn support this feature in which every command executed is treated as the event and is associated with an event number using which they can be recalled and changed if required. These commands are saved in a history file. In Bash shell history command shows the whole list of the command.
>$ history
> 
> 1  cd Downloads
    2  sudo chmod +x sensor-intern.sh
    3  ./sensor-intern.sh 
    4  ip addr
    5  snap find pycharm
    6  sudo snap install pycharm-community
    7  sudo snap install pycharm-community --classic
    8  sudo apt install snapd
    9  sudo snap install pycharm-educational --classic
   10  sudo snap install pycharm-community --classic
   11  sudo apt install snapd
   12  sudo snap install pycharm-community --classic

> ## 18. ls 
* The 'ls' command is used to list files and directories. The contents of your current working directory, 

> $ ls
> 
> ushabhat@ushabhat-Latitude-5531:~/Desktop$ ls Demo.txt
Demo.txt
ushabhat@ushabhat-Latitude-5531:~/Desktop$ ls -l
total 4
-rw-rw-r-- 1 ushabhat ushabhat 45 Feb 28 23:38 Demo.txt
ushabhat@ushabhat-Latitude-5531:~/Desktop$ 

> ## 19. man
* man command in Linux is used to display the user manual of any command that we can run on the terminal. 
> $ man printf 
> 
> PRINTF(1)                        User Commands                       PRINTF(1)
> NAME
       printf - format and print data
SYNOPSIS
       printf FORMAT [ARGUMENT]...
       printf OPTION
DESCRIPTION
       Print ARGUMENT(s) according to FORMAT, or execute according to OPTION:

       --help display this help and exit

       --version
              output version information and exit

> ## 20. mkdir
* The mkdir stands for 'make directory'. 
With the help of mkdir command, you can create a new directory wherever you want in your system. Just type "mkdir <dir name> , in place of <dir name> type the name of new directory, 
you want to create and then press enter.

>$ mkdir <directory name>
> 
> ushabhat@ushabhat-Latitude-5531:~/Desktop$ mkdir newDesktop
ushabhat@ushabhat-Latitude-5531:~/Desktop$ ls
Demo.txt  newDesktop

> ## 21. rm
* Use the rm command to remove files you no longer need. 

> $ rm
> 
> ushabhat@ushabhat-Latitude-5531:~/Desktop$ rm Demo.txt
ushabhat@ushabhat-Latitude-5531:~/Desktop$ ls
newDesktop

> ## 22. mv
* mv stands for move. mv is used to move one or more files or directories from one place to another in a file system like UNIX. It has two distinct functions: 
1. It renames a file or folder. 
2. It moves a group of files to a different directory.

> $ mv <filename>
> 
>ushabhat@ushabhat-Latitude-5531:~/Desktop$ ls
a.txt  b.txt  Demo.txt  newDesktop
ushabhat@ushabhat-Latitude-5531:~/Desktop$ mv a.txt geek.txt
ushabhat@ushabhat-Latitude-5531:~/Desktop$ ls
b.txt  Demo.txt  geek.txt  newDesktop

> ## 23. passwd
* The passwd command changes passwords for user accounts.

> $ passwd
> 
> ushabhat@ushabhat-Latitude-5531:~/Desktop$ passwd
Changing password for ushabhat.
Current password: 
New password: 
Retype new password: 
passwd: password updated successfully

> ## 24. shutdown
* The shutdown command in Linux is used to shutdown the system in a safe way. You can shutdown the machine immediately, or schedule a shutdown using 24 hour format.

> $ sudo shutdown  
> 
> ushabhat@ushabhat-Latitude-5531:~/Desktop$ sudo shutdown 18:30
[sudo] password for ushabhat: 
Shutdown scheduled for Wed 2023-03-01 18:30:00 IST, use 'shutdown -c' to cancel.

> ## 25.ssh
* ssh stands for “Secure Shell”. It is a protocol used to securely connect to a remote server/system. ssh is secure in the sense that it transfers the data in encrypted form between the host and the client. It transfers inputs from the client to the host and relays back the output. ssh runs at TCP/IP port 22.

>$ ssh-keygen
> 
> ushabhat@ushabhat-Latitude-5531:~/Desktop$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/ushabhat/.ssh/id_rsa): Documents
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in Documents
Your public key has been saved in Documents.pub
The key fingerprint is:
SHA256:w7YHiyrgDWybRPYtvr5ExTaCI9VL3WvsaXQNStiulAA ushabhat@ushabhat-Latitude-5531
The key's randomart image is:
+---[RSA 3072]----+
|  Eo . +         |
| .. = o + .      |
|.o o B = o o     |
|.o. = +.B . .    |
|+ .... =So       |
|.=.o ..o+=       |
|+.*.. ..o .      |
| +oo .   .       |
|  .=+            |
+----[SHA256]-----+

> ## 26. scp
* scp (secure copy) command in Linux system is used to copy file(s) between servers in a secure way. The SCP command or secure copy allows secure transferring of files in between the local host and the remote host or between two remote hosts.
* It uses the same authentication and security as it is used in the Secure Shell (SSH) protocol. SCP is known for its simplicity, security and pre-installed availability.

> $ scp <options>
> 
> shabhat@ushabhat-Latitude-5531:~/Desktop$ scp -P
option requires an argument -- P
usage: scp [-346BCpqrTv] [-c cipher] [-F ssh_config] [-i identity_file]
            [-J destination] [-l limit] [-o ssh_option] [-P port]
            [-S program] source ... target


> ## 27. rsync
* rsync or remote synchronization is a software utility for Unix-Like systems that efficiently sync files and directories between two hosts or machines. One of them being the source or the local-host from which the files will be synced, the other one being the remote-host, on which synchronization will take place.

> $ rsync <options> source <destinations>
> 
> ushabhat@ushabhat-Latitude-5531:~/Desktop$ rsync /home/
drwxr-xr-x          4,096 2023/02/28 22:45:08 .
drwxr-xr-x          4,096 2023/02/28 22:45:08 newuser
drwxr-xr-x          4,096 2023/02/28 03:23:04 username
drwxr-xr-x          4,096 2023/03/02 10:46:25 ushabhat

> ## 28. ps
* Linux provides us a utility called ps for viewing information related with the processes on a system which stands as abbreviation for “Process Status”.

> $ ps 
> 
> ushabhat@ushabhat-Latitude-5531:~/Desktop$ ps
    PID TTY          TIME CMD
   6764 pts/0    00:00:00 bash
   7419 pts/0    00:00:00 ps

> ## 29.dir
* dir command differs from ls command in the format of listing contents that is in default listing options.
By default, dir command lists the files and folders in columns, sorted vertically and special characters are represented by backslash escape sequences.

> $ dir <options> 
> 
> ushabhat@ushabhat-Latitude-5531:~/Desktop$ dir -a
.  ..  Demo.txt

> ## 30. tail 
* It is the complementary of head command.The tail command, as the name implies, print the last N number of data of the given input. By default it prints the last 10 lines of the specified files. If more than one file name is provided then data from each file is precedes by its file name.

> $ tail <filename>
> 
> ushabhat@ushabhat-Latitude-5531:~/Desktop$ cat> Demo.txt
1
2
3
4
5
6
7
8
9
0
11
12
13
14
^C
ushabhat@ushabhat-Latitude-5531:~/Desktop$ tail Demo.txt
5
6
7
8
9
0
11
12
13
14

> ## 31. touch
* The touch command is a standard command used in UNIX/Linux operating system which is used to create, change and modify timestamps of a file.

> $ touch 
> 
> ushabhat@ushabhat-Latitude-5531:~/Desktop$ touch Demo.txt
ushabhat@ushabhat-Latitude-5531:~/Desktop$ ls
Demo.txt
ushabhat@ushabhat-Latitude-5531:~/Desktop$ ll
total 12
drwxr-xr-x  2 ushabhat ushabhat 4096 Mar  2 11:12 ./
drwxr-xr-x 21 ushabhat ushabhat 4096 Mar  2 10:46 ../
-rw-rw-r--  1 ushabhat ushabhat   33 Mar  2 11:48 Demo.txt

> ## 32. uname
* The command ‘uname‘ displays the information about the system.
* -a option: It prints all the system information in the following order: Kernel name, network node hostname, kernel release date, kernel version, machine hardware name, hardware platform, operating system.

>uname <option>
> 
> ushabhat@ushabhat-Latitude-5531:~/Desktop$ uname -a
Linux ushabhat-Latitude-5531 5.14.0-1033-oem #36-Ubuntu SMP Mon Apr 4 15:15:49 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux

>## 32.which 
* which command in Linux is a command which is used to locate the executable file associated with the given command by searching it in the path environment variable. It has 3 return status as follows:

0 : If all specified commands are found and executable.

1 : If one or more specified commands is nonexistent or not executable.

2 : If an invalid option is specified.

>$ which <filename> <filename2>
> 
> ushabhat@ushabhat-Latitude-5531:~/Desktop$ which cpp python java
/usr/bin/cpp





 









