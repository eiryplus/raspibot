from slackbot.bot import respond_to     # @botname: で反応するデコーダ
# from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ

from common.camera import take_a_photo


def upload_photo(message):
    file_path = take_a_photo()
    message.channel.upload_file(fname="photo.jpg", fpath=file_path)


@respond_to("take a photo")
def func1(message):
    upload_photo(message)
