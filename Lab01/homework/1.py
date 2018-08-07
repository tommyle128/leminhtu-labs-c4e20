from gmail import *
import random

import datetime
time_now = datetime.datetime.now()

reasons = [
    "đi chơi bạn gái",
    "bị ốm nặng",
    "phải về quê",
    "đi đám cưới",
    "có việc đột xuất"
]

choose_reason = random.choice(reasons)


gmail = GMail('Tu Le<tulm.test@gmail.com>','congacon')

html_content ="""
<p style="text-align: center;"><strong>Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</strong></p>
<p style="text-align: center;"><strong>Độc lập - Tự do - Hạnh ph&uacute;c</strong></p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><span style="color: #ff0000;"><strong>ĐƠN XIN NGHỈ HỌC</strong></span></p>
<p style="text-align: left;">Ch&agrave;o thầy, m&igrave;nh l&agrave; T&uacute;.</p>
<p style="text-align: left;">M&igrave;nh viết đơn n&agrave;y xin thầy cho nghỉ học. L&iacute; do của e nghỉ học l&agrave;: {{li_do}}</p>
<p style="text-align: left;"><img style="display: block; margin-left: auto; margin-right: auto;" src="https://media.giphy.com/media/fH3LbssRHBIxSu6vf7/giphy.gif" /></p>
<p style="text-align: left;">Cảm ơn thầy đ&atilde; tạo điều kiện :)</p>
"""

msg = Message('HTML Email - Don xin nghi hoc',to='<tulm.test@gmail.com>', html= html_content.replace("{{li_do}}", choose_reason))

if time_now.hour > 7 or (time_now.hour == 7 and (time_now.minute > 0 or time_now.second > 0)):
    gmail.send(msg)