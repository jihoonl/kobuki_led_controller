import subprocess

def play_sound(resource_path, sound):
    chirp_path = subprocess.check_output(['rospack','find','kobuki_utils']).replace('\n','')
    chirp = chirp_path + '/scripts/chirp.bash' 
    sound_path = resource_path + '/' + sound
    subprocess.call([chirp, sound_path])
