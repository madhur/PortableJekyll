/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
#ifndef __GLADE_ATTRIBUTES_H__
#define __GLADE_ATTRIBUTES_H__

#include <glib-object.h>
#include <gladeui/glade.h>

G_BEGIN_DECLS


#define GLADE_TYPE_EPROP_ATTRS            (glade_eprop_attrs_get_type())
#define	GLADE_TYPE_ATTR_GLIST             (glade_attr_glist_get_type())

/* The GladeParamSpecAttributes is a GList * of GladeAttribute structs */
typedef struct _GladeAttribute             GladeAttribute;

struct _GladeAttribute {
	PangoAttrType   type;   /* The type of pango attribute */

	GValue          value;  /* The coresponding value */

	guint           start;  /* The text offsets where the attributes should apply to */
	guint           end;
};


GType        glade_eprop_attrs_get_type         (void) G_GNUC_CONST;
GType        glade_attr_glist_get_type          (void) G_GNUC_CONST;

GladeAttribute *glade_gtk_attribute_from_string (PangoAttrType    type,
						 const gchar     *strval);
gchar       *glade_gtk_string_from_attr         (GladeAttribute  *gattr);
void         glade_attr_list_free               (GList           *attrs);


G_END_DECLS

#endif   /* __GLADE_ATTRIBUTES_H__ */
