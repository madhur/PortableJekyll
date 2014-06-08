/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
#ifndef __GLADE_SIGNAL_H__
#define __GLADE_SIGNAL_H__

#include <glib.h>

G_BEGIN_DECLS


#define GLADE_SIGNAL(s) ((GladeSignal *)s)
#define GLADE_IS_SIGNAL(s) (s != NULL)

typedef struct _GladeSignal  GladeSignal;

struct _GladeSignal
{
	gchar    *name;         /* Signal name eg "clicked"            */
	gchar    *handler;      /* Handler function eg "gtk_main_quit" */
	gchar    *userdata;     /* User data signal handler argument   */

	gchar    *support_warning;/* Message to inform the user about signals introduced in future versions */
	
	guint8    after : 1;    /* Connect after TRUE or FALSE         */
	guint8    swapped : 1;  /* Connect swapped TRUE or FALSE (GtkBuilder only) */
};


GladeSignal *glade_signal_new   (const gchar *name,
				 const gchar *handler,
				 const gchar *userdata,
				 gboolean     after,
				 gboolean     swapped);

GladeSignal *glade_signal_clone (const GladeSignal *signal);
void         glade_signal_free  (GladeSignal *signal);

gboolean     glade_signal_equal (GladeSignal *sig1, GladeSignal *sig2);

GladeSignal *glade_signal_read  (GladeXmlNode *node);
void         glade_signal_write (GladeSignal        *signal,
				 GladeProjectFormat  fmt,
				 GladeXmlContext    *context,
				 GladeXmlNode       *node);

void         glade_signal_set_support_warning (GladeSignal *signal,
					       const gchar *support_warning);

G_END_DECLS

#endif /* __GLADE_SIGNAL_H__ */
