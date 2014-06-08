/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
#ifndef __GLADE_BUILTINS_H__
#define __GLADE_BUILTINS_H__

#include <glib-object.h>
#include <gladeui/glade.h>

G_BEGIN_DECLS

typedef struct _GladeParamSpecObjects   GladeParamSpecObjects;


#define GLADE_TYPE_STOCK               (glade_standard_stock_get_type())
#define GLADE_TYPE_STOCK_IMAGE         (glade_standard_stock_image_get_type())
#define	GLADE_TYPE_GLIST               (glade_glist_get_type())
#define	GLADE_TYPE_PARAM_OBJECTS       (glade_param_objects_get_type())
#define GLADE_TYPE_ITEM_APPEARANCE     (glade_item_appearance_get_type())

#define GLADE_IS_STOCK(pspec) \
        (G_TYPE_CHECK_INSTANCE_TYPE ((pspec), GLADE_TYPE_STOCK))

#define GLADE_IS_STOCK_IMAGE(pspec) \
        (G_TYPE_CHECK_INSTANCE_TYPE ((pspec), GLADE_TYPE_STOCK_IMAGE))

#define GLADE_IS_PARAM_SPEC_OBJECTS(pspec)     \
        (G_TYPE_CHECK_INSTANCE_TYPE ((pspec),  \
         GLADE_TYPE_PARAM_OBJECTS))
#define GLADE_PARAM_SPEC_OBJECTS(pspec)        \
        (G_TYPE_CHECK_INSTANCE_CAST ((pspec),  \
         GLADE_TYPE_PARAM_OBJECTS, GladeParamSpecObjects))

GType        glade_standard_stock_get_type       (void) G_GNUC_CONST;
GType        glade_standard_stock_image_get_type (void) G_GNUC_CONST;
GType        glade_glist_get_type                (void) G_GNUC_CONST;
GType        glade_param_objects_get_type        (void) G_GNUC_CONST;
GType        glade_item_appearance_get_type      (void) G_GNUC_CONST;

GParamSpec  *glade_param_spec_objects      (const gchar   *name,
					    const gchar   *nick,
					    const gchar   *blurb,
					    GType          accepted_type,
					    GParamFlags    flags);

void         glade_param_spec_objects_set_type (GladeParamSpecObjects *pspec,
						GType                  type);
GType        glade_param_spec_objects_get_type (GladeParamSpecObjects *pspec);

GParamSpec  *glade_standard_pixbuf_spec      (void);
GParamSpec  *glade_standard_gdkcolor_spec    (void);
GParamSpec  *glade_standard_objects_spec     (void);
GParamSpec  *glade_standard_stock_spec       (void);
GParamSpec  *glade_standard_stock_image_spec (void);
GParamSpec  *glade_standard_int_spec         (void);
GParamSpec  *glade_standard_uint_spec        (void);
GParamSpec  *glade_standard_string_spec      (void);
GParamSpec  *glade_standard_strv_spec        (void);
GParamSpec  *glade_standard_float_spec       (void);
GParamSpec  *glade_standard_boolean_spec     (void);

void         glade_standard_stock_append_prefix (const gchar *prefix);

G_END_DECLS

#endif   /* __GLADE_BUILTINS_H__ */
