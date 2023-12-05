import os

video_directory = "./videos"

os.system("cls")

for filename in os.listdir(video_directory):
    if filename.endswith(".webm"):
        name = os.path.splitext(filename)[0]

        html = f"""
    <div class="grid-item">
        <video oncontextmenu="return false;" controls poster="./video-previews/{name}.png">
            <source src="./videos/{name}.webm" type="video/webm">
        </video>
        <div class="footer">
            <h3>{name}</h3>
            <a download href="./videos/{name}.webm" class="download-btn">Download</a>
        </div>
    </div>
        """

        print(html)
