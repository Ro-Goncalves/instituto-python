import requests
import m3u8
import os
from urllib.parse import urljoin
import re

def download_subtitles(m3u8_url, output_file='subtitles.vtt'):
    """
    Download subtitles from an M3U8 playlist and combine them into a single VTT file.
    
    Args:
        m3u8_url (str): URL of the M3U8 playlist containing subtitles
        output_file (str): Name of the output file (default: subtitles.vtt)
    """
    try:
        # Download and parse the M3U8 playlist
        response = requests.get(m3u8_url)
        response.raise_for_status()
        
        playlist = m3u8.loads(response.text)
        
        if not playlist.segments:
            raise ValueError("No segments found in the M3U8 playlist")
        
        # Create a temporary directory for segment files
        temp_dir = "temp_subtitles"
        os.makedirs(temp_dir, exist_ok=True)
        
        # Download and combine all subtitle segments
        full_content = ""
        segment_number = 0
        
        # Get base URL for relative paths
        base_url = m3u8_url.rsplit('/', 1)[0] + '/'
        
        print(f"Downloading {len(playlist.segments)} subtitle segments...")
        
        for segment in playlist.segments:
            # Handle both absolute and relative URLs
            segment_url = segment.uri if segment.uri.startswith('http') else urljoin(base_url, segment.uri)
            
            response = requests.get(segment_url)
            response.raise_for_status()
            
            content = response.text
            
            # For the first segment, keep the WebVTT header
            if segment_number == 0:
                full_content += content
            else:
                # For subsequent segments, skip the WebVTT header
                content_without_header = re.sub(r'^WEBVTT\n\n', '', content)
                full_content += content_without_header
            
            segment_number += 1
            print(f"Downloaded segment {segment_number}/{len(playlist.segments)}")
        
        # Write the combined content to the output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        # Clean up temporary directory
        os.rmdir(temp_dir)
        
        print(f"\nSubtitles successfully downloaded and saved to {output_file}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading subtitles: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def vtt_to_text_formatted(vtt_content):
    """
    Convert VTT subtitle content to plain text dialogue with line breaks after periods.
    
    Args:
        vtt_content (str): The content of the VTT file
    
    Returns:
        str: Formatted string with dialogue, one sentence per line
    """
    # Primeiro, vamos verificar o conteúdo recebido
    print("Conteúdo original:")
    print(vtt_content)
    print("\n---\n")
    
    # Remover o cabeçalho WEBVTT e metadata de forma mais simples
    lines = vtt_content.split('\n')
    dialogue_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Pular linhas vazias e cabeçalhos
        if line == '' or line.startswith('WEBVTT') or line.startswith('X-TIMESTAMP'):
            i += 1
            continue
            
        # Pular número da legenda
        if line.isdigit():
            i += 1
            continue
            
        # Pular timestamp (procura por --> no texto)
        if '-->' in line:
            i += 1
            continue
            
        # Se chegamos aqui, é uma linha de diálogo
        if line:
            dialogue_lines.append(line)
        i += 1
    
    # Juntar todas as linhas
    full_dialogue = ' '.join(dialogue_lines)
    
    # Limpar espaços múltiplos
    full_dialogue = re.sub(r'\s+', ' ', full_dialogue)
    
    # Adicionar quebras de linha após pontos finais
    formatted_dialogue = re.sub(r'\. ', '.\n\n', full_dialogue.strip())
    
    return formatted_dialogue

def process_vtt_file(file_path):
    """
    Process a VTT file and return formatted dialogue.
    
    Args:
        file_path (str): Path to the VTT file
    
    Returns:
        str: Formatted dialogue
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return vtt_to_text_formatted(content)
    except UnicodeDecodeError:
        # Tentar com encoding diferente se utf-8 falhar
        with open(file_path, 'r', encoding='latin-1') as file:
            content = file.read()
            return vtt_to_text_formatted(content)
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")
        return None




if __name__ == "__main__":
    # URL da legenda do seu exemplo
    subtitle_url = "https://dyckms5inbsqq.cloudfront.net/crewAI/C2/L2/subtitle/eng/sc-crewAI-C2-L2-eng.m3u8"

    download_subtitles(subtitle_url, "output_subtitles.vtt")
    
    # Extrair o diálogo formatado
    file_path = 'output_subtitles.vtt'  # Substitua pelo caminho do seu arquivo
    formatted_dialogue = process_vtt_file(file_path)

    if formatted_dialogue:
        print("\nDiálogo formatado:")
        print(formatted_dialogue)
        
        # Salvar em um arquivo
        with open('dialogo_formatado.md', 'w', encoding='utf-8') as file:
            file.write(formatted_dialogue)

   