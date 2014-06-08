#include <ruby.h>

#ifndef RSTRING_PTR
#define RSTRING_PTR(str) (RSTRING(str)->ptr)
#endif

extern struct stemmer * create_stemmer(void);
extern void free_stemmer(struct stemmer * z);
extern int stem(struct stemmer * z, char * b, int k);

/* copied from porter.c */
struct stemmer {
	char * b;       /* buffer for word to be stemmed */
	int k;          /* offset to the end of the string */
	int j;          /* a general offset into the string */
};

static VALUE stem_word(VALUE self, VALUE arg)
{
	size_t length, i;
	char *word;
	struct stemmer z;
	VALUE str, rv;

	str = StringValue(arg);
	word = malloc(RSTRING_LEN(str) + 1);
	strncpy(word, RSTRING_PTR(str), RSTRING_LEN(str));
	word[RSTRING_LEN(str)] = '\0';

	length  = stem(&z, word, strlen(word)-1);
	word[length+1] = 0;
	rv = rb_str_new2(word);
	free(word);
	return rv;
}

VALUE mStemmer;

void Init_stemmer(void) {
	mStemmer = rb_define_module("Stemmer");
	rb_define_module_function(mStemmer, "stem_word", stem_word, 1);
}
