import imageio

image_files = ['2.jpg', '3.jpg', '4.jpg']

with imageio.get_writer('ciktienyeniy.gif', mode='I', duration=4.0) as writer:
    for filename in image_files:
        image = imageio.imread(filename)
        writer.append_data(image)

print("GIF başarıyla oluşturuldu: ciktienyeniy.gif 🎉")



