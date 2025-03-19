import yt_dlp

def get_video_info(url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'force_generic_extractor': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        title = info.get('title', 'unknown_title')
        channel = info.get('uploader', 'unknown_channel')
        video_id = info.get('id', 'unknown_id')
        return title, channel, video_id

def download_ydl(url, ydl_opts):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      info = ydl.extract_info(url, download=True)

def main():
    status_processamento = ["------- TRABALHANDO -------\n"]

    # Solicita o link do vídeo ao usuário
    video_url = input("Cole o link do vídeo e aperte Enter: ")    

    #Obtém o título, nome do canal e o ID do vídeo
    video_title, channel_name, video_id = get_video_info(video_url)

    status_processamento.append("INFORMAÇÕES SOBRE O VÍDEO\n")
    status_processamento.append(f'- Video URL: {video_url}')
    status_processamento.append(f'- Título do vídeo: {video_title}')
    status_processamento.append(f'- Nome do canal: {channel_name}')
    status_processamento.append(f'- Video ID: {video_id}')
    status_processamento.append("\n")
        
    status_processamento.append("STATUS DO PROCESSAMENTO\n")

        
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            #'merge_output_format': 'mp4'
        }
        download_ydl(video_url, ydl_opts)       

        status_processamento.append("- Arquivo MP4 baixado com sucesso!")
        print("\n".join(status_processamento))

    except Exception as e:      
        status_processamento.append(f"Erro ao baixar o arquivo: {e}")
        print("\n".join(status_processamento))

    # try:
    #     print("\n")
    #     # Opções para yt-dlp para baixar apenas o áudio
    #     ydl_opts = {
    #         'format': 'bestaudio/best',
    #         'postprocessors': [{
    #             'key': 'FFmpegExtractAudio',
    #             'preferredcodec': 'mp3',
    #             'preferredquality': '192',
    #         }],           
    #     }

    #     download_ydl(video_url, ydl_opts)
        
    #     status_processamento.append("- Arquivo MP3 baixado com sucesso!")
    #     print("\n".join(status_processamento))

    # except Exception as e:        
    #     status_processamento.append(f"Erro ao baixar o arquivo: {e}")
    #     print("\n".join(status_processamento))

main()