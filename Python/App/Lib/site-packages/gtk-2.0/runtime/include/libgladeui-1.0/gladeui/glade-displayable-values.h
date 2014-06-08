/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
#ifndef __GLADE_DISAPLAYABLE_VALUES_H__
#define __GLADE_DISAPLAYABLE_VALUES_H__

#include <glib.h>
#include <glib-object.h>

G_BEGIN_DECLS

void        glade_register_displayable_value      (GType          type, 
						   const gchar   *value, 
						   const gchar   *domain,
						   const gchar   *string);

void        glade_register_translated_value       (GType          type, 
						   const gchar   *value, 
						   const gchar   *string);

gboolean    glade_type_has_displayable_values     (GType          type);

G_CONST_RETURN 
gchar      *glade_get_displayable_value           (GType          type, 
						   const gchar   *value);

G_CONST_RETURN 
gchar *glade_get_value_from_displayable           (GType          type, 
						   const gchar   *displayabe);

G_END_DECLS

#endif /* __GLADE_DISAPLAYABLE_VALUES_H__ */
