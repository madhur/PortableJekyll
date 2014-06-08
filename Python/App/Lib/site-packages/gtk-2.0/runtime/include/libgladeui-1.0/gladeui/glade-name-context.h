/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
#ifndef __GLADE_NAME_CONTEXT_H__
#define __GLADE_NAME_CONTEXT_H__

#include <glib.h>

G_BEGIN_DECLS

typedef struct _GladeNameContext GladeNameContext;

GladeNameContext  *glade_name_context_new                 (void);
void               glade_name_context_destroy             (GladeNameContext *context);

gchar             *glade_name_context_new_name            (GladeNameContext *context,
							   const gchar      *base_name);

gchar             *glade_name_context_dual_new_name       (GladeNameContext *context,
							   GladeNameContext *another_context,
							   const gchar      *base_name);

guint              glade_name_context_n_names             (GladeNameContext *context);

gboolean           glade_name_context_has_name            (GladeNameContext *context,
							   const gchar      *name);

gboolean           glade_name_context_add_name            (GladeNameContext *context,
							   const gchar      *name);

void               glade_name_context_release_name        (GladeNameContext *context,
							   const gchar      *name);

G_END_DECLS

#endif /* __GLADE_NAME_CONTEXT_H__ */
