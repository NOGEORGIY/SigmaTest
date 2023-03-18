vercel
# -*- coding: utf-8 -*-
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType


def main():
    vk_session = vk_api.VkApi(token='vk1.a.Si1KNE1cgv4wSm9cKQiE2Gx7Munc4I_yfLq_x9YRZ3eENrIECvLAmS4-p1AUHyTm4IGcT8BJwS10ertNqOMivuR63d9wIMQmLSRDe0boejI4UTQPgfbS4SYH5ofEekyLlJSVkHJicOcXBizjMpU_fGrMr7_3Z4o64Jz66Pr7GWs2P7INGkV2b1nDp98nntMKOku8eQl-kXJSrfRPMiYMHQ')
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.to_me:
            if event.type == VkEventType.MESSAGE_NEW:
                id = event.user_id
                if event.text == 'нет':
                    vk_session.method('messages.send', {'user_id': id, 'message': 'я тебя ненавижу', 'random_id': 0})
                if event.text == 'хорошо' or event.text == 'да':
                    vk_session.method('messages.send', {'user_id': id, 'message': 'спасибо!', 'random_id': 0})
                vk_session.method('messages.send', {'user_id': id, 'message':'дай денег', 'random_id':0})
main()
