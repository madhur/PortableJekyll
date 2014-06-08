/* -*- Mode: C; c-basic-offset: 4 -*-
 * libglade - a library for building interfaces from XML files at runtime
 * Copyright (C) 1998-2002  James Henstridge <james@daa.com.au>
 *
 * glade-xml.h: public interface of libglade library
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Library General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Library General Public License for more details.
 *
 * You should have received a copy of the GNU Library General Public
 * License along with this library; if not, write to the 
 * Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 * Boston, MA  02111-1307, USA.
 */
#ifndef GLADE_XML_H
#define GLADE_XML_H

#include <glib.h>
#include <gtk/gtk.h>

G_BEGIN_DECLS

#define GLADE_TYPE_XML            (glade_xml_get_type())
#define GLADE_XML(obj)            (G_TYPE_CHECK_INSTANCE_CAST ((obj), GLADE_TYPE_XML, GladeXML))
#define GLADE_XML_CLASS(klass)    (G_TYPE_CHECK_CLASS_CAST ((klass), GLADE_TYPE_XML, GladeXMLClass))
#define GLADE_IS_XML(obj)         (G_TYPE_CHECK_INSTANCE_TYPE ((obj), GLADE_TYPE_XML))
#define GLADE_IS_XML_CLASS(klass) (G_TYPE_CHECK_CLASS_TYPE ((obj), GLADE_TYPE_XML))
#define GLADE_XML_GET_CLASS(obj)  (G_TYPE_INSTANCE_GET_CLASS((obj), GLADE_TYPE_XML, GladeXMLClass))

typedef struct _GladeXML GladeXML;
typedef struct _GladeXMLClass GladeXMLClass;
typedef struct _GladeXMLPrivate GladeXMLPrivate;

struct _GladeXML {
    /* <public> */
    GObject parent;

    char *filename;

    /* <private> */
    GladeXMLPrivate *priv;
};

struct _GladeXMLClass {
    GObjectClass parent_class;

    /* Virtual function: gets the appropriate gtype for the typename.*/
    GType (* lookup_type) (GladeXML*self, const char *gtypename);
};

GType      glade_xml_get_type            (void);
GladeXML  *glade_xml_new                 (const char *fname, const char *root,
					  const char *domain);
GladeXML  *glade_xml_new_from_buffer     (const char *buffer, int size,
					  const char *root,
					  const char *domain);
gboolean   glade_xml_construct           (GladeXML *self, const char *fname,
					  const char *root,
					  const char *domain);

gboolean   glade_xml_construct_from_buffer (GladeXML *self, const char *buffer, int size,
					  const char *root,
					  const char *domain);

void       glade_xml_signal_connect      (GladeXML *self,
					  const char *handlername,
					  GCallback func);
void       glade_xml_signal_connect_data (GladeXML *self,
					  const char *handlername,
					  GCallback func,
					  gpointer user_data);
/*
 * use gmodule to connect signals automatically.  Basically a symbol with
 * the name of the signal handler is searched for, and that is connected to
 * the associated symbols.  So setting gtk_main_quit as a signal handler
 * for the destroy signal of a window will do what you expect.
 */
void       glade_xml_signal_autoconnect  (GladeXML *self);

/* if the gtk_signal_connect_object behaviour is required, connect_object
 * will point to the object, otherwise it will be NULL.
 */
typedef void (*GladeXMLConnectFunc) (const gchar *handler_name,
				     GObject *object,
				     const gchar *signal_name,
				     const gchar *signal_data,
				     GObject *connect_object,
				     gboolean after,
				     gpointer user_data);

/*
 * These two are to make it easier to use libglade with an interpreted
 * language binding.
 */
void       glade_xml_signal_connect_full     (GladeXML *self,
					      const gchar *handler_name,
					      GladeXMLConnectFunc func,
					      gpointer user_data);

void       glade_xml_signal_autoconnect_full (GladeXML *self,
					      GladeXMLConnectFunc func,
					      gpointer user_data);


GtkWidget *glade_xml_get_widget              (GladeXML *self,
					      const char *name);
GList     *glade_xml_get_widget_prefix       (GladeXML *self,
					      const char *name);

gchar     *glade_xml_relative_file           (GladeXML *self,
					      const gchar *filename);

/* don't free the results of these two ... */
const char *glade_get_widget_name      (GtkWidget *widget);
GladeXML   *glade_get_widget_tree      (GtkWidget *widget);


/* interface for changing the custom widget handling */
typedef GtkWidget *(* GladeXMLCustomWidgetHandler) (GladeXML *xml,
						    gchar *func_name,
						    gchar *name,
						    gchar *string1,
						    gchar *string2,
						    gint int1,
						    gint int2,
						    gpointer user_data);

void glade_set_custom_handler(GladeXMLCustomWidgetHandler handler,
			      gpointer user_data);

#ifndef LIBGLADE_DISABLE_DEPRECATED
#define glade_xml_new_with_domain glade_xml_new
#define glade_xml_new_from_memory glade_xml_new_from_buffer
#endif

G_END_DECLS
	
#endif

