O repositório que você compartilhou abrange **ambos os desafios (Ransomware e Keylogger)**, o que é excelente para demonstrar um entendimento completo sobre diferentes tipos de malwares.

Abaixo está uma sugestão de arquivo **`README.md`** abrangente, estruturado em um formato de portfólio técnico que documenta ambas as simulações, conforme solicitado no desafio.

---

# 🛡️ Projeto de Simulação e Análise de Malwares (Ransomware & Keylogger)

## ⚠️ AVISO DE SEGURANÇA E USO EDUCACIONAL

**Este projeto é estritamente para fins educacionais e de pesquisa em cibersegurança defensiva.** O objetivo é entender os mecanismos de ataque para desenvolver estratégias de proteção eficazes.

* **NUNCA** execute este código em sistemas de produção, redes ativas ou máquinas das quais você não possui permissão expressa.
* **RECOMENDADO:** A execução dos scripts deve ser feita em um **Ambiente Isolado (Máquina Virtual ou Sandbox)**.

---

## 🚀 Visão Geral do Desafio

Este projeto consolida o conhecimento adquirido no curso, simulando em ambiente controlado o comportamento de duas das ameaças cibernéticas mais críticas da atualidade: **Ransomware** (sequestro de dados) e **Keylogger** (captura de dados).

A documentação detalha a implementação em **Python**, as vulnerabilidades exploradas e, o mais importante, as **medidas de prevenção e defesa** para mitigar esses riscos.

## 1. 😈 Módulo Ransomware Simulado

Este módulo demonstra o processo de criptografia e descriptografia de arquivos, simulando um ataque de sequestro de dados.

### 1.1. Implementação em Python (`ransomware.py`)

* **Objetivo:** Criptografar arquivos de teste em um diretório específico e gerar uma nota de resgate simulada, exigindo uma chave para a recuperação dos dados.
* **Tecnologias:** Python, biblioteca **`cryptography`** (módulo **Fernet** para criptografia simétrica).

#### Fluxo de Operação
1.  **Geração de Chave:** Uma chave única é gerada e salva (simulando o controle da chave pelo atacante).
2.  **Criptografia:** O script varre o diretório alvo, lê os arquivos de teste (`.txt`, `.doc`, etc.), os criptografa usando a chave Fernet e os renomeia (ex: adicionando a extensão `.encrypted`).
3.  **Nota de Resgate:** Um arquivo `README_TO_DECRYPT.txt` é gerado, instruindo a vítima a "pagar" para receber a chave de descriptografia.
4.  **Descriptografia (Função de Recuperação):** Uma função separada permite a inserção da chave correta para reverter o processo e restaurar os arquivos originais.

### 1.2. 🛑 Estratégias de Defesa contra Ransomware

* **Backup (Regra 3-2-1):** A defesa mais robusta. Ter pelo menos **três** cópias dos dados, em **dois** tipos diferentes de mídia, com **uma** cópia fora do local (offline ou em nuvem). 
* **Segmentação de Rede:** Limitar o acesso do Ransomware a apenas uma parte da rede.
* **Controle de Acesso:** Implementar o **Princípio do Menor Privilégio (PoLP)** para restringir quem pode modificar ou deletar arquivos críticos.

---

## 2. ⌨️ Módulo Keylogger Simulado

Este módulo simula a captura e a exfiltração de dados digitados pelo usuário.

### 2.1. Implementação em Python (`keylogger.py`)

* **Objetivo:** Capturar as teclas pressionadas e enviar o arquivo de log gerado para um e-mail de teste, simulando o roubo de credenciais.
* **Tecnologias:** Python, biblioteca **`pynput`** (captura de teclado), módulo **`smtplib`** (envio de e-mail).

#### Fluxo de Operação
1.  **Escuta:** O `Listener` da `pynput` é iniciado e opera em segundo plano.
2.  **Registro:** As teclas são registradas em um arquivo local (`log.txt`).
3.  **Exfiltração:** Após um intervalo de tempo predefinido, o script usa o `smtplib` para estabelecer uma conexão com um servidor SMTP e envia o `log.txt` para o endereço de e-mail do atacante simulado.

### 2.2. 🕵️ Estratégias de Defesa contra Keyloggers

* **Firewall e Filtros de Rede:** Bloquear o tráfego de saída (SMTP) de processos não autorizados, impedindo a fase de **exfiltração**.
* **Monitoramento de Processos (EDR):** Identificar processos incomuns ou scripts sendo executados em segundo plano, que estão realizando chamadas de API do teclado.
* **Autenticação Multifator (MFA):** Mesmo que a senha seja capturada, o MFA impede o login, pois o atacante não terá o segundo fator.
* **Gerenciadores de Senhas:** Usar o preenchimento automático para evitar a digitação manual de credenciais, impedindo a captura pelo Keylogger.

---

## 3. 🧠 Reflexão Geral sobre Defesa

A melhor defesa contra a maioria dos malwares combina **Tecnologia** e **Conscientização**. 

| Defesa | Nível de Proteção | Função Principal |
| :--- | :--- | :--- |
| **Tecnológico** | **Endpoint (Computador)** | **Antivírus/EDR:** Identificação de padrões de arquivos e comportamento heurístico. |
| **Tecnológico** | **Perímetro (Rede)** | **Firewall:** Bloqueio de portas de exfiltração (ex: SMTP) e conexões não autorizadas. |
| **Tecnológico** | **Isolamento** | **Sandboxing / Máquinas Virtuais:** Execução de códigos ou arquivos suspeitos em ambiente seguro e isolado. |
| **Humano** | **Primeira Linha de Defesa** | **Treinamento e Conscientização:** Prevenção contra Engenharia Social, Phishing e instalação inicial do malware. |

## 🔗 Recursos e Próximos Passos

Este repositório serve como prova de conceito para:

* Demonstrar a implementação de malwares em Python.
* Analisar os pontos de falha no ataque.
* Propor soluções de defesa proativas.

**Próximos Passos:**
1.  Adicionar um script de **Ofuscação** básica para o Keylogger para dificultar a detecção.
2.  Implementar o registro do **Ransomware (e a chave)** em um arquivo criptografado para simular o ataque de ponta a ponta.

> 🧑‍💻 Desenvolvido por [Luiza Stefanello] - [11/25]# ransware_keylogger
