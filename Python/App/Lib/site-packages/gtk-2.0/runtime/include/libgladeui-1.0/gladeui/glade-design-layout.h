/*
 * glade-design-layout.h
 *
 * Copyright (C) 2006-2007 Vincent Geddes
 *
 * Authors:
 *   Vincent Geddes <vgeddes@gnome.org>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 */

#ifndef __GLADE_DESIGN_LAYOUT_H__
#define __GLADE_DESIGN_LAYOUT_H__

#include <gtk/gtk.h>

G_BEGIN_DECLS

#define GLADE_TYPE_DESIGN_LAYOUT              (glade_design_layout_get_type ())
#define GLADE_DESIGN_LAYOUT(obj)              (G_TYPE_CHECK_INSTANCE_CAST ((obj), GLADE_TYPE_DESIGN_LAYOUT, GladeDesignLayout))
#define GLADE_DESIGN_LAYOUT_CLASS(klass)      (G_TYPE_CHECK_CLASS_CAST ((klass), GLADE_TYPE_DESIGN_LAYOUT, GladeDesignLayoutClass))
#define GLADE_IS_DESIGN_LAYOUT(obj)           (G_TYPE_CHECK_INSTANCE_TYPE ((obj), GLADE_TYPE_DESIGN_LAYOUT))
#define GLADE_IS_DESIGN_LAYOUT_CLASS(klass)   (G_TYPE_CHECK_CLASS_TYPE ((klass), GLADE_TYPE_DESIGN_LAYOUT))
#define GLADE_DESIGN_LAYOUT_GET_CLASS(obj)    (G_TYPE_INSTANCE_GET_CLASS ((obj), GLADE_TYPE_DESIGN_LAYOUT, GladeDesignLayoutClass))

typedef struct _GladeDesignLayout         GladeDesignLayout;
typedef struct _GladeDesignLayoutPrivate  GladeDesignLayoutPrivate;
typedef struct _GladeDesignLayoutClass    GladeDesignLayoutClass;

enum
{
	GLADE_WIDGET_EVENT_STOP_EMISSION   = 1 << 0,
	GLADE_WIDGET_EVENT_RETURN_TRUE     = 1 << 1
};

struct _GladeDesignLayout
{
	GtkBin parent_instance;

	GladeDesignLayoutPrivate *priv;
};

struct _GladeDesignLayoutClass
{
	GtkBinClass parent_class;
	gboolean      (*widget_event)        (GladeProject *project,
					      GladeWidget *gwidget,
					      GdkEvent *event);

};


GType        glade_design_layout_get_type     (void) G_GNUC_CONST;

GtkWidget   *glade_design_layout_new          (void);

gboolean     glade_design_layout_widget_event (GladeDesignLayout *layout,
                                               GladeWidget       *event_gwidget,
                                               GdkEvent          *event);


G_END_DECLS

#endif /* __GLADE_DESIGN_LAYOUT_H__ */
