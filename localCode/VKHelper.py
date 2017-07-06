# -*- coding: utf-8 -*-
import vk


class VKHelper():
    ALICE_ID = 32897432
    MISHA_ID = 34499244
    MY_ID = 303154598

    def __init__(self, psw):
        self.session = vk.AuthSession('5229876', 'aoklyunin@yandex.ru', psw, scope='wall, messages')
        self.vk_api = vk.API(self.session, v='5.35', lang='ru')

    def wallPost(self, s):
        self.vk_api.wall.post(message=s)

    def sendMessage(self, s, u_id):
        self.vk_api.messages.send(user_id=u_id, message=s)

    def sendMessageWithPicture(self,s,u_id,pic):
        self.vk_api.messages.send(user_id=u_id, message=s,attachment=pic)
