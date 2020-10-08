#include <stdlib.h>
#include <stdio.h>
#include <string.h>


void inicializar (Lista **l) {
	*l = NULL;
}

int inserir_inteiro (Lista **l, int chave, int val) {
	Lista *aux, *novo;

	novo = (Lista*)malloc(sizeof(Lista));
	novo->info = malloc(sizeof(int));
	*((int*)novo->info) = val;
	novo->chave = chave;
	novo->tipo = 'i';
	
	if (*l == NULL) {
		*l = novo;
		novo->prox = novo;
		novo->ant = novo;
		return 1;
	}
	if ((*l)->chave > chave) {
		(*l)->prox = novo;
		(*l)->ant = novo;
		novo->prox = (*l);
		novo->ant = (*l);
		(*l) = novo;
		return 1;
	}
	aux = *l;
	while ((aux->prox != (*l)) && (aux->prox->chave < chave)) 
		aux = aux->prox;
	
	if ((aux->prox)->chave == chave) {
		free(novo->info);
		free(novo);
		return 0;
	}
	
	novo->prox = aux->prox;
	novo->ant = aux;
	(aux->prox)->ant = novo;
	aux->prox = novo;
	return 1;
}

int inserir_p_flutuante (Lista **l, int chave, float val) {
	Lista *aux, *novo;

	novo = (Lista*)malloc(sizeof(Lista));
	novo->info = malloc(sizeof(float));
	*((float*)novo->info) = val;
	novo->chave = chave;
	novo->tipo = 'f';
	
	if (*l == NULL) {
		*l = novo;
		novo->prox = novo;
		novo->ant = novo;
		return 1;
	}
	if ((*l)->chave > chave) {
		(*l)->prox = novo;
		(*l)->ant = novo;
		novo->prox = (*l);
		novo->ant = (*l);
		(*l) = novo;
		return 1;
	}
	aux = *l;
	while ((aux->prox != (*l)) && (aux->prox->chave < chave)) 
		aux = aux->prox;
	
	if ((aux->prox)->chave == chave) {
		free(novo->info);
		free(novo);
		return 0;
	}
	
	novo->prox = aux->prox;
	novo->ant = aux;
	(aux->prox)->ant = novo;
	aux->prox = novo;
	return 1;
}
int inserir_c_caracteres (Lista **l, int chave, char *val) {
	Lista *aux, *novo;

	novo = (Lista*)malloc(sizeof(Lista));
	novo->info = malloc((strlen(val)+1)*sizeof(char));
	strcpy ( (char*)(novo->info) , val);
	novo->chave = chave;
	novo->tipo = 's';
	
	if (*l == NULL) {
		*l = novo;
		novo->prox = novo;
		novo->ant = novo;
		return 1;
	}
	if ((*l)->chave > chave) {
		(*l)->prox = novo;
		(*l)->ant = novo;
		novo->prox = (*l);
		novo->ant = (*l);
		(*l) = novo;
		return 1;
	}
	aux = *l;
	while ((aux->prox != (*l)) && (aux->prox->chave < chave)) 
		aux = aux->prox;
	
	if ((aux->prox)->chave == chave) {
		free(novo->info);
		free(novo);
		return 0;
	}
	
	novo->prox = aux->prox;
	novo->ant = aux;
	(aux->prox)->ant = novo;
	aux->prox = novo;
	return 1;
}

int inserir_caractere (Lista **l, int chave, char val) {
	Lista *aux, *novo;

	novo = (Lista*)malloc(sizeof(Lista));
	novo->info = malloc(sizeof(char));
	*((char*)novo->info) = val;
	novo->chave = chave;
	novo->tipo = 'c';
	
	if (*l == NULL) {
		*l = novo;
		novo->prox = novo;
		novo->ant = novo;
		return 1;
	}
	if ((*l)->chave > chave) {
		(*l)->prox = novo;
		(*l)->ant = novo;
		novo->prox = (*l);
		novo->ant = (*l);
		(*l) = novo;
		return 1;
	}
	aux = *l;
	while ((aux->prox != (*l)) && (aux->prox->chave < chave)) 
		aux = aux->prox;
	
	if ((aux->prox)->chave == chave) {
		free(novo->info);
		free(novo);
		return 0;
	}
	
	novo->prox = aux->prox;
	novo->ant = aux;
	(aux->prox)->ant = novo;
	aux->prox = novo;
	return 1;
}

char obter_tipo (Lista *l, int chave) {
	Lista *aux;

	if (l == NULL)
		return 0;	
	aux = l;
	
	while ((aux->chave != chave) && (aux->prox != l))
		aux = aux->prox;
		
	if (aux->chave == chave)
		return aux->tipo;
	else
		return 0;
}

int obter_inteiro (Lista *l, int chave) {
	Lista *aux;

	if (l == NULL)
		return 0;	
	aux = l;
	
	while ((aux->chave != chave) && (aux->prox != l))
		aux = aux->prox;
		
	if (aux->chave == chave) {
		if (obter_tipo(l, chave) == 'i')
			return *((int*)aux->info);
		else
			return -99999;
	} else
		return -99999;
}

float obter_p_flutuante (Lista *l, int chave) {
	Lista *aux;

	if (l == NULL)
		return 0;	
	aux = l;
	
	while ((aux->chave != chave) && (aux->prox != l))
		aux = aux->prox;
		
	if (aux->chave == chave) {
		if (obter_tipo(l, chave) == 'f')
			return *((float*)aux->info);
		else
			return -99999.0;
	} else
		return -99999.0;
}
char *obter_c_caracteres (Lista *l, int chave) {
	Lista *aux;

	if (l == NULL)
		return 0;	
	aux = l;
	
	while ((aux->chave != chave) && (aux->prox != l))
		aux = aux->prox;
		
	if (aux->chave == chave) {
		if (obter_tipo(l, chave) == 's')
			return ((char*)aux->info);
		else
			return NULL;
	} else
		return NULL;
}

char obter_caractere (Lista *l, int chave) {
	Lista *aux;

	if (l == NULL)
		return 0;	
	aux = l;
	
	while ((aux->chave != chave) && (aux->prox != l))
		aux = aux->prox;
		
	if (aux->chave == chave) {
		if (obter_tipo(l, chave) == 'c')
			return *((char*)aux->info);
		else
			return -99999.0;
	} else
		return -99999.0;
}

void listar_elementos (Lista *l) {
	Lista *aux;
	
	aux = l;
	if (aux != NULL)
		do {
			switch(aux->tipo) {
				case 'i':
					printf("Chave: %d - Tipo: Int - Valor: %d\n", aux->chave, *((int*)(aux->info)));
					break;
				case 'f':
					printf("Chave: %d - Tipo: Float - Valor: %f\n", aux->chave, *((float*)(aux->info)));
					break;
				case 'c':
					printf("Chave: %d - Tipo: Char - Valor: %c\n", aux->chave, *((char*)(aux->info)));
					break;
				case 's':
					printf("Chave: %d - Tipo: Cadeia - Valor: %s\n", aux->chave, ((char*)(aux->info)));
					break;
			}
			aux = aux->prox;
		} while(aux != l);
}

int main(int narg, char *argv[]) {
	Lista *ll;
	
	inicializar(&ll);
	
	if (inserir_inteiro(&ll, 10, 123))
		printf("Insercao de int ok\n");
	
	if (inserir_p_flutuante(&ll, 3, 123.456))
		printf("Insercao de float ok\n");
	
	if (inserir_caractere(&ll, 15, 'P'))
		printf("Insercao de char ok\n");	
		
	if (inserir_c_caracteres(&ll, 12, "Ivo"))
		printf("Insercao de string ok\n");	
	
	if (inserir_inteiro(&ll, 15, 123123))
		printf("Insercao de int ok\n");
	else
		printf("Insercao do 2o int com erro\n");	
		
	listar_elementos(ll);

	printf("Tipo do elemento de chave 3: %c\n", obter_tipo(ll, 3));
	printf("Tipo do elemento de chave 15: %c\n", obter_tipo(ll, 15));
	printf("Tipo do elemento de chave 18: %c\n", obter_tipo(ll, 18));
	printf("Tipo do elemento de chave 10: %c\n", obter_tipo(ll, 10));
	
	printf("Obtendo inteiro da chave 10: %d\n", obter_inteiro(ll, 10));
	printf("Obtendo inteiro da chave 3: %d\n", obter_inteiro(ll, 3));
	
	
	return EXIT_SUCCESS;
}



















