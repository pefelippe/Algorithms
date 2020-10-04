
#include <iostream>

using namespace std;

template <typename T> 
struct Noh { 
	T elem;
	Noh<T> *esq, *dir; 
};

template <typename T> 
struct Arvore { 
	Noh<T> *raiz; 
};

template <typename T>
void inicializar (Arvore<T> &A) {
	A.raiz = nullptr; 
}

template <typename T> 
bool pertence (Arvore<T> &A, T e) // Retorno: e A? ∈ A?
{
	if (A.raiz == nullptr) return false;
	if(A.raiz->elem == e) return true;
	if(A.raiz->elem > e) pertence<T>(A.raiz->esq, e);
	else
		pertence<T>(A.dir, e);

}
template <typename T>
bool inserir (Arvore<T> &A, T e) // Pré-cond.: e A.
{

}
int main(int argc, char const *argv[])
{
	Arvore<int> arv;
	inicializar(arv);
	pertence(arv, 10);

	return 0;
}