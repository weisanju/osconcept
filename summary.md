# Part One-overview

## Introduction

an operating system is  a program that manages the computer hardware. It also provide the basis for application programs and acts as an intermediary betwteen the user and the computer hardware

操作系统是 管理计算机硬件的程序,它也为应用程序提供了基础,在用户和计算机硬件中起到 中间媒介的作用

An amazing aspect of operating system is how varied they are in accomplishing these taskes

操作系统令人惊叹的一面 是他们完成这些交互任务的方式 多种多样

Mainframe operating systems are designed primarily to optimize utilization 
of hardware. 

大型主机操作系统 主要为 了优化硬件的使用率 而设计的



Personal computer (PC) operating systems support complex 
games, business applications, and everything in between. 

PC操作系统 提供复杂游戏,商业应用 以及介于两者之间的所有

 Operating systems for handheld computers are designed to provide an environment in which a 
user can easily interface with the computer to execute programs. 

手持电脑的操作系统 旨在提供一种环境,让用户轻松与计算机交互以执行程序

Thus, some 
operating systems are designed to be convenient, others to be efficient, and others 
some combination of the two. 

因此,一些操作系统被设计为方便,其他的被设计为高效,而还有一些则两者特点都有

Before we can explore the details of computer system operation, we need 
to know something about system structure. 

在我们探索计算机系统操作的细节之前,我们需要了解关于系统架构的东西

We begin by discussing the basic 
functions of system startup, I/0, and storage. 

我们先从 系统启动,IO,存储的 基本功能开始讨论

We also describe the basic 
computer architecture that makes it possible to write a functional operating 
system. 

我们同样描述了基本的计算机架构,这些架构使得 写一个功能性的操作系统 成为可能

Because an operating system is large and complex, it must be created 
piece by piece.

因为 一个操作系统是非常庞大且复杂的,它必须一块块创建

 Each of these pieces should be a well-delineated portion of the  system, with carefully defined inputs, outputs, and functions. 

每一块都应是 系统中系统明确描述的部分,带有经过仔细定义了的输入,输出和功能

In this chapter, 
we provide a general overview of the major components of an operating 
system. 

在这个章节中,我们提供了 一个操作系统的主要组成部分的大体上的描述



## CHAPTER OBJECTIVES

章节目标

To provide a grand tour of the major components of operating systems. 

提供一个 对操作系统主要组成部分 的全面介绍

To describe the basic organization of computer systems. 

描述 计算机系统的基本 组成

## 1.1 What Operating System Do

We begin our discussion by looking at the operating system's role in the 
overall computer system.

我们从 研究操作系统在整个 计算机系统中的作用来 开始讨论

 A computer system can be divided roughly into 
four components: the hardware/ the operating system, the application programs/ 
and the users

计算机系统可以大致划分成四个组成部分:硬件/操作系统/应用程序/用户

The hardware- central processing unit,the memory ,and the input/output(I/O) devices provides the basic computing resources for the system.

硬件-CPU,内存,IO设备 提供了基本的计算资源

The application program as word processors/ spreadsheets/ compilers, and Web browsers - define the ways in which these resources are used to solve users' computing problems. 

The operating system controls the 
hardware and coordinates its use among the various application programs for 
dsfdfd 

the various users. 
We can also view a computer system as consisting of hardware/ software/ 
and data. The operating system provides the means for proper use of these 
resources in the operation of the computer system. An operating system is 
similar to a government. Like a government, it performs no useful function by 
itself. It simply provides an environment within which other programs can do 
useful work. 
To understand more fully the operating systemfs role, we next explore 
operating systems from two viewpoints: that of the user and that of the system. 
1.1.1 User View 
The user's view of the computer varies according to the interface being 
used. Most computer users sit in front of a PC, consisting of a monitor/ 
keyboard/ mouse, and system unit. Such a system is designed for one user 
to monopolize its resources. The goal is to maximize the work (or play) that 
the user is performing. In this case/ the operating system is designed mostly 
for with some attention paid to performance and none paid 
to various hardware and software resources are 
shared. Performance is, of course, important to the user; but such systems 
1.1 5 
are optimized for the single-user experience rather than the requirements of 
multiple users. 
In other cases, a user sits at a terminal connected to a or a 
Other users are accessing the sance computer through other 
terminals. These users share resources and may exchange information. The 
operating system in S"Llclc cases is designed to maximize resource utilization￾to assure that all available CPU time, memory, and I/0 are used efficiently and 
tbat no individual user takes more than her fair share. 
In still otber cases, users sit at connected to networks of 
other workstations and These users have dedicated resources at their 
disposal, but they also share resources such as networking and servers-file, 
compute, and print servers. Therefore, their operating system is designed to 
compromise between individual usability and resource utilization. 
Recently, many varieties of handheld computers have come into fashion. 
Most of these devices are standalone units for individual users. Some are 
connected to networks, either directly by wire or (more often) through wireless 
modems and networking. Because of power, speed, and interface limitations, 
they perform relatively few remote operations. Their operating systems are 
designed mostly for individual usability, but performance per unit of battery 
life is important as well. 
Some computers have little or no user view. For example, embedded 
computers in home devices and automobiles may have numeric keypads and 
may turn indicator lights on or off to show status, but they and their operating 
systems are designed primarily to run without user intervention. 
1.1.2 System View 
From the computer's point of view, the operating system is the program 
most intimately involved with the hardware. In this context, we can view 
an operating system as a . A computer system has many 
resources that may be required to solve a problem: CPU time, memory space, 
file-storage space, I/0 devices, and so on. The operating system acts as the 
manager of these resources. Facing numerous and possibly conflicting requests 
for resources, the operating system must decide how to allocate them to specific 
programs and users so that it can operate the computer system efficiently and 
fairly. As we have seen, resource allocation is especially important where many 
users access the same mainframe or minicomputer. 
A slightly different view of an operating system emphasizes the need to 
control the various I/0 devices and user programs. An operating system is a 
control program. A manages the execution of user programs 
to prevent errors and improper use of the computer. It is especially concerned 
with the operation and control of I/O devices. 
1.1.3 Defining Operating Systems 
We have looked at the operating system's role from the views of the user 
and of the system. How, though, can we define what an operating system 
is? In general, we have no completely adequate definition of an operating 
system. Operating systems exist because they offer a reasonable way to solve 
the problem of creating a usable computing system. The fundamental goal 
of computer systems is to execute user programs and to make solving user 
6 Chapter 1 
1.2 
STORAGE DEFINITIONS AND NOTATION 
A is the basic unit of computer storage. It can contain one of two values, 
zero and one. All other storage in a computer is based on collections of bits. 
Given enough bits, it is amazing how many things a computer can represent: 
numbers, letters, images, movies, sounds, documents, and programs, to name 
a few. A is 8 bits, and on most computers it is the smallest convenient 
chunk of storage. For example, most computers don't have an instruction 
to move a bit but do have one to move a byte. A less common term is 
which is a given computer architecture's native storage unit. A word is 
generally made up of one or more bytes. For example, a computer may have 
instructions to move 64-bit (8-byte) words. 
A kilobyte, or KB, is 1,024 bytes; a megabyte, or MB, is 1,0242 bytes; and 
a gigabyte, or GB, !s 1,0243 bytes. Computer manufacturers often round off 
these numbers and say that a megabyte is 1 million bytes and a gigabyte is 1 
billion bytes. 
problems easier. Toward this goal, computer hardware is constructed. Since 
bare hardware alone is not particularly easy to use, application programs are 
developed. These programs require certain common operations, such as those 
controlling the II 0 devices. The common functions of controlling and allocating 
resources are then brought together into one piece of software: the operating 
system. 
In addition, we have no universally accepted definition of what is part of the 
operating system. A simple viewpoint is that it includes everything a vendor 
ships when you order "the operating system." The features included, however, 
vary greatly across systems. Some systems take up less than 1 megabyte of 
space and lack even a full-screen editor, whereas others require gigabytes of 
space and are entirely based on graphical windowing systems. A more common 
definition, and the one that we usually follow, is that the operating system 
is the one program running at all times on the computer-usually called 
the . (Along with the kernel, there are two other types of programs: 
which are associated with the operating system but are not 
part of the kernel, and which include all programs not 
associated with the operation of the system.) 
The matter of what constitutes an operating system has become increas￾ingly important. In 1998, the United States Deparhnent of Justice filed suit 
against Microsoft, in essence claiming that Microsoft included too much func￾tionality in its operating systems and thus prevented application vendors from 
competing. For example, a Web browser was an integral part of the operating 
systems. As a result, Microsoft was found guilty of using its operating-system 
monopoly to limit competition. 
Before we can explore the details of how computer systems operate, we need 
general knowledge of the structure of a computer system. In this section, 
we look at several parts of this structure. The section is mostly concerned 
1.2 
THE STUDY OFOPERATING SYSTEMS 
There has neverbeenarnore interestirighnwtostud yoperating systems:· and 
it has neverb.een.e~sier.Theopen-sourc;e movernent has overtaken .operating 
systems, caJ.tsing marly ofthenctobemadeavailable in both source and binary 
(e~ecuta]Jle) fonnat.·.This Iistindud~~Linu)(, BSDUNIX/Solat•is,and part of• 
]\II~cos.x. Th~availa~ilityqf·source.code.q,llowsus.tostudyoperq,til}.gsy?tems 
frorrt theinsid,eout' .. Questionsthat previo)1sly could onlyb~ answerecL~y 
looking atdocumentaticmor thebehayior.ofan op~rating system c.annow be 
answered by examining the code itself. 
In additi?n,. the rise of virtualization as a ll}.ainsfreafll. ( andfrequelltly free) 
cmnp)1ter ftmctionmakesitpos;~i1Jlet()runnmnyoperqtingsystems.ontop.of 
onecoresystem .. Forexample,VMware(J:lttp.://www .• vmwarE:).com):provides 
afree·''player'' on which hundreds.of free .''virtualappliilnces'' cann.m.Using 
this method,students call tryolit hundreds. ofoperatingsystems.withintheir 
existing operatingsystems .atno cost. ... ··. . .. .·. ·.. · ... · 
Operating .sy~temsthat are no lortge~ ~ofllmerci~lly viableltave been 
opell-~o}lrced asvvell, ·enablirtg·.usto study how system~ pperated i~< 
time.of•.•f~v.r~r CPU, ll}.emory,•·•etnd.storcrge•·•·.resoJ.trces,·····.An ... exten~iye.b).It·•not 
complete .•. list ()f 9pen'-sourct operafirtg-"system pr?j~?ts is .. availa~le £rom 
ht~p :// dm()~ ' org/ C:omp)1ters/Softp(lre /Operati»g:-Systems/p~~m._Sourc~/-
S. i.m .. • .. •· .. ·.u. l·a·t·o . .rs.•· .. o··.f······s·· .. P ... e ... c .. i.fi .. ·.·c·· .. ··. ·•.h ..... a ... ·.r ... ·.d ...• w ... •·.a .•. r ... e ..... ·.· .... ar .. e· ... · .a·l·s·o .. · ...... a·.··v ... •· ... a.il .. ·<1. b ... ·.·.le·· ... ·.i·n···.· .. · ... · ... s .. om .•. ·. · .. e. •.·.c.·.· .... a····.·s·e· s. '···· ... al .. I.·.o ....... w.· .•.. m.· .•··.g .. th~ operat~<g systell}.to.runon.''na~ve''.hardware, ... all~ithrrtthec?l}.fines 
of a modem CO!TIPJ-Iter and moderJ1 OPf/'atirtg ~ystem. For: example, a 
DECSYSTEMc20 simulator running on Mac OS X can boot TOPS-20, loa~. the 
~ource.tages;.·and modify al'ld comp~le·<l·.J:t.evvTOPS-20 .k~rneL ··Art·interested 
stltdent ~ar• search theint~rnet to find the origillal papers that de~cribe the 
operating systemand .. the.origipa~ manuals: 
Tl<e adve~t?fogen-source operafirtg sy~te1Tis also l}."lal<es it easy t?··.make 
the move fromstu~enttooper<:lting~systemdeveloper.With some knov.rledge, 
som~ effo1't, a11d an Internet connection,a student c;al'leven create a new 
operating-systemdistribution! Justa. fev.r years, ~go itwas diffic]_llt or 
if1Lpossible ··to. get acce~s·. to ·source co?e . . N?v.r·. that access is.·liJnited only 
bylt()wmuchtimeand disk space a student has. · 
7 
with computer-system organization, so you can skim or skip it if you already 
understand the concepts.







计算机系统组织

计算机系统架构

开放操作系统架构

开放操作系统操作

进程管理

内存管理

存储管理

保护与安全

分布式系统

专用用途系统

计算环境


开源操作系统
 








