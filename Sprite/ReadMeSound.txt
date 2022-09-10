pg.mixer.music.load("#путь") - pзагрузка файла в проект(ФОРМАТ WAV,OGG,MP3)

pg.mixer.music.play(#количество проигрышей(-1 - бесконечно),#время старта в секундах, #время начала затухания музыки) - воспроизведение музыки
pg.mixer.music.pause() - ставит на паузу
pg.mixer.music.unpause() - снимает с паузы
pg.mixer.music.rewind() - начинает музыку с начала
pg.mixer.music.stop() - полностью отсанавливает музыку
pg.mixer.music.set_volume(vol) - устанавливает громкость музыки ( от 0 до 1)
pg.mixer.music.get_volume() - возвращает громкость музыки


s1 = pg.mixer.Sound("Sound/gamesound.wav") - создание звука для проигрывания в многопоточном режиме(ФОРМАТ WAV,OGG)
ch1 = s1.play() - создание канала