/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
#ifndef __GLADE_PARAMETER_H__
#define __GLADE_PARAMETER_H__

G_BEGIN_DECLS

/* The GladeParameter is a pair of a key and a value. It is used by the
 * GladeSetting object. We store in a string the value no matter the
 * type of the paramter it is. This adds "extra" information to a
 * GladeProperty that we can blindly parse/set/query
 * The valid parameter keys depend on the type of the property

     <Property>
      <Type>Integer</Type>
	 .....
	 <Parameters>
	   <Parameter Key="Min" Value="0"/>
	   <Parameter Key="Max" Value="10000"/>
	   <Parameter Key="Default" Value="0"/>
	   <Parameter Key="StepIncrement" Value="1"/>
	   <Parameter Key="PageIncrement" Value="10"/>
	   <Parameter Key="ClimbRate" Value="1"/>
	 </Parameters>
    </Property>

 */
typedef struct _GladeParameter   GladeParameter;

struct _GladeParameter {

	gchar *key;   /* The name of the parameter */
	gchar *value; /* The textual representation of the parameter */
};

 
GladeParameter *glade_parameter_new (void);

GladeParameter *glade_parameter_clone (GladeParameter *parameter);

void            glade_parameter_free (GladeParameter *parameter);

void            glade_parameter_get_float   (GList *parameters, const gchar *key, gfloat *value);

void            glade_parameter_get_integer (GList *parameters, const gchar *key, gint *value);

void            glade_parameter_get_boolean (GList *parameters, const gchar *key, gboolean *value);

void            glade_parameter_get_string  (GList *parameters, const gchar *key, gchar **value);

GList *         glade_parameter_list_new_from_node (GList *list, GladeXmlNode *node);

G_END_DECLS

#endif /* __GLADE_PARAMETER_H__ */
