#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/* ESTRUTURA DE DADOS */

/* cria a matriz e aponta cada elemento (casa) pra baixo, cima, esquerda e direita */
matriz_t * matriz_criar(int linhas, int colunas) {
    setlocale(LC_CTYPE, ""); 

    int linha = 0;
    int coluna = 0;
    
    /* ponteiros auxiliares para setar as structs*/
    elemento_t * temp = NULL;
    elemento_t * prim = NULL; 
    elemento_t * aux_baixo = NULL; 
    elemento_t * aux_cima = NULL;
    elemento_t * inicio = NULL; //vai apontar pra primeira posicao da matriz posteriormente

    for( linha = 0; linha < linhas; linha++ ) {
        temp= NULL;

        for( coluna = 0; coluna < colunas; coluna++ ) {
            elemento_t * elemento = (elemento_t*) calloc( 1, sizeof(elemento_t) ); //aloca espaco para elemento


            if(!inicio) {//se o inicio for null, inicio recebe o primeiro elemento
                inicio = elemento;
                elemento->esquerda = NULL;
            }
            if(temp)
                temp->direita = elemento;
                
            elemento->esquerda = temp;
            temp = elemento;
        
            if( aux_baixo ) {
                int i = 0;
                elemento_t * aux = aux_baixo; //auxiliar recebe o primeiro da linha de cima

                for( i = 0; i < coluna; i++ )
                    aux = aux->direita;

                aux->abaixo = elemento;
                elemento->cima = aux;
            }

            if( coluna == 0 )
                prim = elemento;

            if(linha == 0)
                temp->cima = NULL;
                     
        }
        //ao pular de linha, o aux_baixo aponta para o primeiro elemento da linha de cima
        aux_baixo = prim;
    }

    matriz_t * m = (matriz_t*) calloc( 1, sizeof(matriz_t) );

    m->inicio = inicio;
    m->colunas = colunas;
    m->linhas = linhas;

    return m;
}
