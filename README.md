# Assinatura Digital com Tkinter

Este projeto consiste em dois aplicativos Tkinter que se complementam para criar e aplicar assinaturas digitais em documentos PDF. O primeiro aplicativo permite desenhar assinaturas e salvá-las como PNG transparente, e o segundo aplicativo permite carregar esses arquivos de assinatura e aplicá-los em documentos PDF.

# Aplicativo 1: Desenhar Assinaturas

## Funcionalidades
- Permite desenhar uma assinatura usando o mouse.
- Salva a assinatura como um arquivo PNG com fundo transparente.
- Limpa a última ação desenhada ou o canvas completo.

# Como Usar
1. Execute o script `OpenSingMaker.py`:
   ```bash
   python OpenSingMaker.py
   ```
2. Use o mouse para desenhar a assinatura no canvas.
3. Clique em "Salvar Assinatura" para salvar a assinatura como um arquivo PNG.
4. Clique em "Limpar Última Ação" para desfazer a última ação desenhada.
5. Clique em "Limpar" para limpar todo o canvas.

# Aplicativo 2: Aplicar Assinaturas em PDF

## Funcionalidades
- Carrega um documento PDF.
- Carrega uma imagem de assinatura (PNG) previamente criada.
- Permite posicionar a assinatura sobre o PDF.
- Salva o PDF com a assinatura aplicada na posição desejada.

### Como Usar
1. Execute o script `OpenPdfSinger.py`:
   ```bash
   python OpenPdfSinger.py
   ```
2. Clique em "Carregar PDF" para selecionar um documento PDF.
3. Clique em "Carregar Assinatura" para selecionar uma imagem de assinatura PNG.
4. Use o mouse para posicionar a assinatura no PDF.
5. Clique em "Salvar PDF Assinado" para salvar o PDF com a assinatura aplicada.
6. Use os botões "Página Anterior" e "Próxima Página" para navegar entre as páginas do PDF.

## Usando os Aplicativos Juntos

Esses dois aplicativos se complementam ao fornecer uma solução completa para a criação e aplicação de assinaturas digitais em documentos PDF:

1. **Criação da Assinatura:** Use o primeiro aplicativo (`OpenSingMaker.py`) para desenhar e salvar a sua assinatura como um arquivo PNG transparente.
2. **Aplicação da Assinatura:** Use o segundo aplicativo (`OpenPdfSinger.py`) para carregar o documento PDF e aplicar a assinatura criada no local desejado.

Dessa forma, você pode criar uma assinatura personalizada e usá-la facilmente em qualquer documento PDF.

---

By Brrxis Codes

---
