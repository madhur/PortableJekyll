/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
#ifndef __GLADE_ACCELS_H__
#define __GLADE_ACCELS_H__

#include <gladeui/glade.h>
#include <gtk/gtk.h>

G_BEGIN_DECLS

#define	GLADE_TYPE_ACCEL_GLIST         (glade_accel_glist_get_type())
#define GLADE_TYPE_EPROP_ACCEL         (glade_eprop_accel_get_type())


#define GLADE_TAG_ACCEL             "accelerator"
#define GLADE_TAG_ACCEL_KEY         "key"
#define GLADE_TAG_ACCEL_MODIFIERS   "modifiers"
#define GLADE_TAG_ACCEL_SIGNAL      "signal"

#define GLADE_TAG_ACCEL_GROUPS "accel-groups"
#define GLADE_TAG_ACCEL_GROUP  "group"


typedef struct _GladeKey                GladeKey;
typedef struct _GladeAccelInfo          GladeAccelInfo;

struct _GladeAccelInfo {
    guint key;
    GdkModifierType modifiers;
    gchar *signal;
};

struct _GladeKey {
	guint  value;
	gchar *name;
};

extern const GladeKey GladeKeys[];

#define  GLADE_KEYS_LAST_ALPHANUM    "9"
#define  GLADE_KEYS_LAST_EXTRA       "questiondown"
#define  GLADE_KEYS_LAST_KP          "KP_9"
#define  GLADE_KEYS_LAST_FKEY        "F35"

GType        glade_accel_glist_get_type    (void) G_GNUC_CONST;
GType        glade_eprop_accel_get_type    (void) G_GNUC_CONST;

GList       *glade_accel_list_copy         (GList         *accels);
void         glade_accel_list_free         (GList         *accels);

gchar       *glade_accels_make_string      (GList *accels);

GladeAccelInfo *glade_accel_read           (GladeXmlNode     *node,
					    gboolean          require_signal);
GladeXmlNode   *glade_accel_write          (GladeAccelInfo   *accel_info,
					    GladeXmlContext  *context,
					    gboolean          write_signal);

G_END_DECLS

#endif   /* __GLADE_ACCELS_H__ */
