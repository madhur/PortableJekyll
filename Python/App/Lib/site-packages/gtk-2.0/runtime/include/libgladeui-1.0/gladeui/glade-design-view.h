/*
 * glade-design-view.h
 *
 * Copyright (C) 2006 Vincent Geddes
 *
 * Authors:
 *   Vincent Geddes <vincent.geddes@gmail.com>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANDESIGN_VIEWILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 */
 
#ifndef __GLADE_DESIGN_VIEW_H__
#define __GLADE_DESIGN_VIEW_H__

#include <gladeui/glade.h>
#include <gladeui/glade-project.h>
#include <gladeui/glade-design-layout.h>

#include <gtk/gtk.h>

G_BEGIN_DECLS

#define GLADE_TYPE_DESIGN_VIEW              (glade_design_view_get_type ())
#define GLADE_DESIGN_VIEW(obj)              (G_TYPE_CHECK_INSTANCE_CAST ((obj), GLADE_TYPE_DESIGN_VIEW, GladeDesignView))
#define GLADE_DESIGN_VIEW_CLASS(klass)      (G_TYPE_CHECK_CLASS_CAST ((klass), GLADE_TYPE_DESIGN_VIEW, GladeDesignViewClass))
#define GLADE_IS_DESIGN_VIEW(obj)           (G_TYPE_CHECK_INSTANCE_TYPE ((obj), GLADE_TYPE_DESIGN_VIEW))
#define GLADE_IS_DESIGN_VIEW_CLASS(klass)   (G_TYPE_CHECK_CLASS_TYPE ((klass), GLADE_TYPE_DESIGN_VIEW))
#define GLADE_DESIGN_VIEW_GET_CLASS(obj)    (G_TYPE_INSTANCE_GET_CLASS ((obj), GLADE_TYPE_DESIGN_VIEW, GladeDesignViewClass))

typedef struct _GladeDesignView         GladeDesignView;
typedef struct _GladeDesignViewPrivate  GladeDesignViewPrivate;
typedef struct _GladeDesignViewClass    GladeDesignViewClass;

struct _GladeDesignView
{
	GtkVBox parent_instance;

	GladeDesignViewPrivate *priv;
};

struct _GladeDesignViewClass
{
	GtkVBoxClass parent_class;

};


GType              glade_design_view_get_type         (void) G_GNUC_CONST;

GtkWidget         *glade_design_view_new              (GladeProject *project);

GladeProject      *glade_design_view_get_project      (GladeDesignView *view);

GladeDesignView   *glade_design_view_get_from_project (GladeProject *project);

GladeDesignLayout *glade_design_view_get_layout       (GladeDesignView *view);


G_END_DECLS

#endif /* __GLADE_DESIGN_VIEW_H__ */
