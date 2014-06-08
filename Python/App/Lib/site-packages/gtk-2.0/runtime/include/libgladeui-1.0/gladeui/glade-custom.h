/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
#ifndef __GLADE_CUSTOM_H__
#define __GLADE_CUSTOM_H__

#include <gladeui/glade.h>
#include <gtk/gtk.h>

G_BEGIN_DECLS

#define GLADE_TYPE_CUSTOM            (custom_get_type ())
#define GLADE_CUSTOM(obj)            (G_TYPE_CHECK_INSTANCE_CAST ((obj), GLADE_TYPE_CUSTOM, GladeCustom))
#define GLADE_CUSTOM_CLASS(klass)    (G_TYPE_CHECK_CLASS_CAST ((klass), GLADE_TYPE_CUSTOM, GladeCustomClass))
#define GLADE_IS_CUSTOM(obj)         (G_TYPE_CHECK_INSTANCE_TYPE ((obj), GLADE_TYPE_CUSTOM))
#define GLADE_IS_CUSTOM_CLASS(klass) (G_TYPE_CHECK_CLASS_TYPE ((klass), GLADE_TYPE_CUSTOM))
#define GLADE_CUSTOM_GET_CLASS(obj)  (G_TYPE_INSTANCE_GET_CLASS ((obj), GLADE_TYPE_CUSTOM, GladeCustomClass))

#define GLADE_CUSTOM_WIDTH_REQ    20
#define GLADE_CUSTOM_HEIGHT_REQ   20

/* taken from glade 2 */
static char * custom_xpm[] = {
"8 8 4 1",
"       c None",
".      c #BBBBBB",
"+      c #D6D6D6",
"@      c #6B5EFF",
".+..+...",
"+..@@@..",
"..@...++",
"..@...++",
"+.@..+..",
".++@@@..",
"..++....",
"..++...."};


typedef struct _GladeCustom      GladeCustom;
typedef struct _GladeCustomClass GladeCustomClass;

struct _GladeCustom
{
	GtkWidget widget;

	GdkPixmap *custom_pixmap;
	
	
};

struct _GladeCustomClass
{
	GtkWidgetClass parent_class;
};

/* Since the class is called Custom and not GladeCustom, 
 * glade-widget-class will search for custom_get_type() instead
 * if glade_custom_get_type()
 */ 
GType  custom_get_type  (void) G_GNUC_CONST;

G_END_DECLS

#endif /* __GLADE_CUSTOM_H__ */
