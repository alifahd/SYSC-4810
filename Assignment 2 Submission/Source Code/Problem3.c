#include <stdio.h>
#include <openssl/bn.h>
void printBN(char *msg, BIGNUM * a) {
	char * number_str = BN_bn2hex(a);
	printf("%s %s", msg, number_str);
	OPENSSL_free(number_str);
}
int main () {
	BN_CTX *ctx = BN_CTX_new();
	BIGNUM *d = BN_new();
	BIGNUM *p = BN_new();
	BIGNUM *q = BN_new();
	BIGNUM *e = BN_new();
	BIGNUM *n = BN_new();
	BIGNUM *tn = BN_new();
	BIGNUM *res1 = BN_new();
	BIGNUM *res2 = BN_new();
	const BIGNUM *BN_value_one(void);
	
	// Initialize p, q, e
	BN_hex2bn(&p, "D40C38D7074F8557BF520C0AA31D6DC3");
	BN_hex2bn(&q, "5AF21620C416E47AFF4C3AEF880C772B");
	BN_hex2bn(&e, "1C901");
	
	// n = p*q
	BN_mul(n, p, q, ctx);
	printBN("\nn = a*b = ", n);
	
	//totient of n (tn)
	BN_sub(res1, p, BN_value_one());
	BN_sub(res2, q, BN_value_one());
	BN_mul(tn, res1, res2, ctx);
	printBN("\ntotient of n = ",tn);
	
	// finding private key: d
	BN_mod_inverse(d, e, tn, ctx);
	printBN("\nd*e mod tn where d = ", d);
	
	printBN("\nPrvaite Key = (", d);
	printBN(", ", n);
	printf(")\n");
	return 0;
}
