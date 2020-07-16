# unbgames

UnBGames é uma plataforma para vizualização e disponibilização para download dos trabalhos finais resultantes da disciplinas de jogos da Universidade de Brasília, produzidos por meio de uma colaboração entre os estudantes dos cursos de Design, Música e Ciência da Computação/Engenharia de Software.


## Instalação

#### Dependências

- Docker
- npm

#### Docker

Construa a imagem com o comando:
```bash
docker build -t unbgames/unbgames-app .
```

Executa o container com:
```bash
docker run -it -p 8080:8080 --rm --name unbgames-app unbgames/unbgames-app
# Vizualize a plataforma em : http://localhost:8080/
```

#### Manual

Para instalar as dependência execute:
```bash
npm install
```

Após a configuração das dependências, para iniciar a aplicação execute:
```bash
npm run serve
# Vizualize a plataforma em : http://localhost:8080/
```

## Licença

Licenciado com GPL v3.0. Veja [LICENSE](https://github.com/unbgames/unbgames/blob/devel/LICENSE) para mais detalhes.
