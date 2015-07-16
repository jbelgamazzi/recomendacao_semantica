##RECOMENDAÇÃO SEMÂNTICA
######UMA ABORDAGEM A RECOMENDAÇÃO DE OBJETOS DE APRENDIZAGEM SEMANTICAMENTE ESTRUTURADOS BASEADO EM FILTRAGEM HÍBRIDA  E PROCESSAMENTO DE LINGUAGEM NATURAL

>* *Este é o inicio do desenvolvimento de um trabalho acadêmico com o intuído de abordar o desenvolvimento de um sistema de recomendação hibrído para ambientes semanticamentes estruturado.*

* Para possibilitar a representação semântica do ambiente, será desenvolvido uma **ontologia** no formato **JSON-LD** seguindo os vocabulários semânticos: (i) **DublinCore:** para representação dos objetos de aprendizagem e (ii) **FOAF:** para presentação de perfis de usuários e seus relacionamentos e interesses.

* Para auxiliar no processo de recomendação de objetos de aprendizagem baseado em seu conteúdo, está sendo desenvolvido um método para extração de keywords relevantes por meio de técnicas de processamento de linguem natural fornecidas pela biblioteca __OpenSource__ **NLTK**.

* O processo de recomendação apresentado neste trabalho será constituído através da interpretação semântica entre os relacionamentos dos perfis de usuários e seus grupos de interesses por meio da linguagem de consulta **SPARQL** amplamentente empregada ao contexto semântico. 



#####INTRODUÇÃO AO TRABALHO

  A disponibilidade de informação para construção de objetos de aprendizagem  em diversas áreas do conhecimento cresce à uma proporção de 40% ao ano [1], facilitada pelo acesso à internet estima que até o ano de 2020 a quantidade de informação do mundo dobrará a cada dois anos [1], aumentando gradativamente a necessidade de recuperar estes objetos de forma eficaz e precisa de acordo com a necessidade e interesse do usuário.
  
  O problema surge quando a recuperação de informações são de responsabilidade dos usuários que por sua vez pode não ter o real conhecimento de suas necessidades de busca, sendo necessário empregar o uso de mecanismos inteligentes, tais como sistemas de recomendação, que possam aprender suas necessidades e expectativas individuais para auxiliar no processo decisório.
  
  Sistemas de recomendação auxiliam no aumento da capacidade e eficácia em processos decisórios redirecionando objetos de aprendizagem à possíveis interessados determinados através de analise comportamentais de indivíduos e objetos. Tais sistemas são classificados em três categorias [2], são elas: (i) **Filtragem baseada em conteúdo:** analisa o conteúdo dos objetos que interessaram o individuo no passado para realizar a recomendação de novos objetos [2]; (ii) **Filtragem colaborativa:** busca predizer a avaliação de um determinado individuo para um objeto baseado nas avaliações dos outros indivíduos para o mesmo objeto [3, 4], através da inteligencia coletiva do grupo [5, 6]; e, (iii) **Filtragem hibrida:** combina as técnicas anteriores com o objetivo de superar as limitações individuais e potencializar seus benefícios.
  
  Entretanto, grande parte dos objetos de aprendizagem atualmente disponíveis foram projetados para o consumo humano o que dificulta o processamento automatizado por mecanismos inteligentes devido sua constituição heterogênea e não estruturada, impedindo ou dificultando interpretações contextuais através de técnicas de filtragem baseada em conteúdo muitas vezes combinadas à **processamento de linguagem natural (PLN)** para busca e construção de possíveis predições contextuais podendo aumentar gradativamente a complexidade e tempo de resposta de suas consultas.
  
  ######**[...]**
  
  
#####REFERÊNCIAS
	
1. IDC iView, "Big Data, Bigger Digital Shadows, and Biggest Growth in the Far East" Dezembro 2012, patrocinado por EMC.

2. BALABANOVIĆ, M.; SHOHAM, Y. Fab: content-based, collaborative recommendation. Communications of the ACM, v. 40, n. 3, p. 66-72, 1997.

3. ADOMAVICIUS, G.; TUZHILIN, A. Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions. Knowledge and Data Engineering, IEEE Transactions on, v. 17, n. 6, p. 734-749, 2005.

4. SARWAR, B. et al. Item-based collaborative filtering recommendation algorithms. Proceedings of the 10th international conference on World Wide Web, 2001. ACM. p.285-295.

5. ALAG, S.; MACMANUS, R. Collective intelligence in action. Manning New York, 2009. ISBN 1933988312.

6. SEGARAN, T. Programming collective intelligence: building smart web 2.0 applications. O'Reilly Media, 2008. ISBN 0596550685.
