from function import *


cl = BE_Team(myToken="",
            myApp="ANDROIDLITE\t2.14.0\tAndroid OS\t5.1.1")
c2 = BE_Team(myToken="",
            myApp="ANDROIDLITE\t2.13.0\tAndroid OS\t6.0.1")
c3 = BE_Team(myToken="",
            myApp="ANDROIDLITE\t2.13.2\tAndroid OS\t7.0")
mid = cl.profile.mid
c1mid = c1.profile.mid
c2mid = c2.profile.mid
creator = ["mid"]
bot = [cl,c1,c2]
botmid = [mid,c1mid,c2mid]
try:
    cl.findAndAddContactsByMid("mid")
    cl.sendMessage("mid", "Ini Sayang")
except:pass
wait = {
"autoJoin": True,
"blacklist":{}
}
proInvite = []
proKick = []
proCancel = []
proQr = []
proJoin = []

def worker(op):
    try:
#=======Auto__Join=========
        if op.type in [13, 124]:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in creator or op.param2 in botmid:
                        cl.acceptChatInvitation(op.param1)
            if c1mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in creator or op.param2 in botmid:
                        c1.acceptChatInvitation(op.param1)
            if c2mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in creator or op.param2 in botmid:
                        c2.acceptChatInvitation(op.param1)
#=======Pro__Invite===========
        if op.type in [13, 124]:
            if op.param1 in proInvite:
                if op.param2 not in creator or botmid:
                    wait["blacklist"][op.param2] = True
                    for invite in op.param3.split('\x1e'):
                        if invite not in creator or botmid:
                            wait["blacklist"][invite] = True
                            random.choice(bot).cancelChatInvitation(op.param1, [invite])
                            random.choice(bot).deleteOtherFromChat(op.param1, [op.param2])
#=======Protect______Kick=========
        if op.type in [19, 133, 32, 126]:
            if op.param1 in proKick:
                if op.param2 not in creator or botmid:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(bot).deleteOtherFromChat(op.param1, [op.param2])
                        random.choice(bot).findAndAddContactsByMid(op.param3)
                        random.choice(bot).inviteIntoChat(op.param1, [op.param3])
                    except:
                        pass
            if op.param1 in proCancel:
                if op.param2 not in creator or botmid:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(bot).deleteOtherFromChat(op.param1, [op.param2])
                        random.choice(bot).findAndAddContactsByMid(op.param3)
                        random.choice(bot).inviteIntoChat(op.param1, [op.param3])
                    except:
                        pass
            if op.param3 in creator and op.param3 in botmid:
                if op.param2 not in creator or botmid:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(bot).deleteOtherFromChat(op.param1, [op.param2])
                        random.choice(bot).findAndAddContactsByMid(op.param3)
                        random.choice(bot).inviteIntoChat(op.param1, [op.param3])
                    except:
                        pass
            if op.type in [11, 122]:
                if op.param1 in proQr:
                    if op.param2 not in creator or botmid:
                            if cl.getChats([op.param1]).chats[0].extra.groupExtra.preventedJoinByTicket == True:
                                try:
                                    wait["blacklist"][op.param2] = True
                                    random.choice(bot).deleteOtherFromChat(op.param1, [op.param2])
                                    chat = random.choice(bot).getChats([op.param1])
                                    if chat.chats[0].extra.groupExtra.preventedJoinByTicket == True:
                                        random.choice(bot).updateChat(chat.chats[0],4)
                                    else:
                                        pass
                                except:
                                    pass
            if op.type in [17, 130]:
                if op.param1 in proJoin:
                    if op.param2 not in creator or botmid:
                            random.choice(bot).deleteOtherFromChat(op.param1, [op.param2])
#===========================
        if op.type in [25, 26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            msg.from_ = msg._from
            sender = msg._from
            cmd = text.lower()
            if msg.toType == 0 and sender != cl.profile.mid: to = sender
            else: to = receiver

            if cmd == "ping":
                if sender in creator:
                    cl.sendMessage(to,'BAWEL')
                    c1.sendMessage(to,'BAWEL')
                    c2.sendMessage(to,'BAWEL')

            if cmd == "speed":
                if sender in creator:
                    start = time.time()
                    cl.sendMessage(to,'benchmark...')
                    total = time.time()-start
                    cl.sendMessage(to,str(total))
                    start = time.time()
                    c1.sendMessage(to,'benchmark...')
                    total = time.time()-start
                    c1.sendMessage(to,str(total))
                    start = time.time()
                    c2.sendMessage(to,'benchmark...')
                    total = time.time()-start
                    c2.sendMessage(to,str(total))

            if cmd == "help":
                if sender in creator:
                    data = """Al-Hadad
> ping
> speed
> help
> joinall
> out
> center out
> proinvite on/off
> prokick on/off
> prokick on/off
> procancel on/off
> proqr on/off
> projoin on/off
> kick @
> banlist
> ceban
                    """
                    cl.sendMessage(to,data)

            if cmd == "joinall":
                if sender in creator:
                    cl.findAndAddContactsByMid(C1mid)
                    cl.findAndAddContactsByMid(C2mid)
                    cl.inviteIntoChat(to, [C1mid,C2mid])
                    c1.acceptChatInvitation(to)
                    c2.acceptChatInvitation(to)

            if cmd == "out":
                if sender in creator:
                    c1.deleteSelfFromChat(to)
                    c2.deleteSelfFromChat(to)

            if cmd == "center out":
                if sender in creator:
                    cl.deleteSelfFromChat(to)

            if cmd == "proinvite on":
                if sender in creator:
                    if to not in proInvite:
                        proInvite.append(to)
                        cl.sendMessage(to, "pro invite aktif")
                    else:
                        cl.sendMessage(to, "pro invite sudah aktif")

            if cmd == "proinvite off":
                if sender in creator:
                    if to in proInvite:
                        proInvite.remove(to)
                        cl.sendMessage(to, "pro invite tidak aktif")
                    else:
                        cl.sendMessage(to, "pro invite sudah tidak aktif")

            if cmd == "prokick on":
                if sender in creator:
                    if to not in proKick:
                        proKick.append(to)
                        cl.sendMessage(to, "pro Kick aktif")
                    else:
                        cl.sendMessage(to, "pro Kick sudah aktif")

            if cmd == "prokick off":
                if sender in creator:
                    if to in proKick:
                        proKick.remove(to)
                        cl.sendMessage(to, "pro Kick tidak aktif")
                    else:
                        cl.sendMessage(to, "pro Kick sudah tidak aktif")

            f cmd == "procancel on":
                if sender in creator:
                    if to not in proCancel:
                        proCancel.append(to)
                        cl.sendMessage(to, "pro Cancel aktif")
                    else:
                        cl.sendMessage(to, "pro Cancel sudah aktif")

            if cmd == "procancel off":
                if sender in creator:
                    if to in proCancel:
                        proCancel.remove(to)
                        cl.sendMessage(to, "pro Cancel tidak aktif")
                    else:
                        cl.sendMessage(to, "pro Cancel sudah tidak aktif")

            if cmd == "proqr on":
                if sender in creator:
                    if to not in proQr:
                        proQr.append(to)
                        cl.sendMessage(to, "pro url aktif")
                    else:
                        cl.sendMessage(to, "pro url sudah aktif")

            if cmd == "proqr off":
                if sender in creator:
                    if to in proQr:
                        proQr.remove(to)
                        cl.sendMessage(to, "pro url tidak aktif")
                    else:
                        cl.sendMessage(to, "pro url sudah tidak aktif")

            if cmd == "projoin on":
                if sender in creator:
                    if to not in proJoin:
                        proJoin.append(to)
                        cl.sendMessage(to, "pro Join aktif")
                    else:
                        cl.sendMessage(to, "pro Join sudah aktif")

            if cmd == "projoin off":
                if sender in creator:
                    if to in proJoin:
                        proJoin.remove(to)
                        cl.sendMessage(to, "pro Join tidak aktif")
                    else:
                        cl.sendMessage(to, "pro Join sudah tidak aktif")

            if cmd.startswith('kick'):
                if msg._from in creator:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for y in targets:
                        if y not in creator and y not in Botmid:
                            try:
                                wait["blacklist"][y] = True
                                random.choice(bot).deleteOtherFromChat(to, [y])
                            except:
                                pass

            if cmd == "banlist":
                if msg._from in creator:
                    if wait["blacklist"] == {}:
                        cl.sendMessage(to, "Not have blacklist")
                    else:
                        mc = "[ Black - List ]\n"
                        a = 0
                        for mid in wait['blacklist']:
                            a = a + 1
                            mc += str(a) + ". " + cl.getContact(mid).displayName + "\n"
                        cl.sendMessage(to,mc)

            if cmd == "ceban":
                if msg._from in creator:
                    ragets = cl.getContacts(wait["blacklist"])
                    mc = "「%i」" % len(ragets)
                    wait["blacklist"] = {}
                    cl.sendMessage(to, mc+": Succes Remove Blacklist")

    except Exception as catch:
        trace = catch.__traceback__
        print("Error Name: "+str(trace.tb_frame.f_code.co_name)+"\nError Filename: "+str(trace.tb_frame.f_code.co_filename)+"\nError Line: "+str(trace.tb_lineno)+"\nError: "+str(catch))

while True:
        try:
            ops = cl.fetchOps()
            for op in ops:
                if op.revision == -1 and op.param2 != None:
                    cl.globalRev = int(op.param2.split("\x1e")[0])
                if op.revision == -1 and op.param1 != None:
                    cl.individualRev = int(op.param1.split("\x1e")[0])
                cl.localRev = max(op.revision, cl.localRev)
                worker(op)
        except:
            pass
            
