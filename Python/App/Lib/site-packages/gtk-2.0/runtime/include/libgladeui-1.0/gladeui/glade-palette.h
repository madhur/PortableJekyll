/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
/*
 * glade-palette.h
 *
 * Copyright (C) 2006 The GNOME Foundation.
 * Copyright (C) 2001-2005 Ximian, Inc.
 *
 * Authors:
 *   Chema Celorio
 *   Joaquin Cuenca Abela <e98cuenc@yahoo.com>
 *   Vincent Geddes <vgeddes@metroweb.co.za>
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

#ifndef __GLADE_PALETTE_H__
#define __GLADE_PALETTE_H__

#include <gladeui/glade.h>

#include <gtk/gtk.h>

G_BEGIN_DECLS

#define GLADE_TYPE_PALETTE              (glade_palette_get_type ())
#define GLADE_PALETTE(obj)              (G_TYPE_CHECK_INSTANCE_CAST ((obj), GLADE_TYPE_PALETTE, GladePalette))
#define GLADE_PALETTE_CLASS(klass)      (G_TYPE_CHECK_CLASS_CAST ((klass), GLADE_TYPE_PALETTE, GladePaletteClass))
#define GLADE_IS_PALETTE(obj)           (G_TYPE_CHECK_INSTANCE_TYPE ((obj), GLADE_TYPE_PALETTE))
#define GLADE_IS_PALETTE_CLASS(klass)   (G_TYPE_CHECK_CLASS_TYPE ((klass), GLADE_TYPE_PALETTE))
#define GLADE_PALETTE_GET_CLASS(obj)    (G_TYPE_INSTANCE_GET_CLASS ((obj), GLADE_TYPE_PALETTE, GladePaletteClass))

typedef struct _GladePalette         GladePalette;
typedef struct _GladePalettePrivate  GladePalettePrivate;
typedef struct _GladePaletteClass    GladePaletteClass;

struct _GladePalette
{
	GtkVBox parent_instance;

	GladePalettePrivate *priv;
};

struct _GladePaletteClass
{
	GtkVBoxClass parent_class;

	void    (* toggled)    (GladePalette *palette);
	void    (* refresh)    (GladePalette *palette);
};

typedef enum
{
	GLADE_ITEM_ICON_AND_LABEL,
	GLADE_ITEM_ICON_ONLY,
	GLADE_ITEM_LABEL_ONLY
} GladeItemAppearance;


GType                glade_palette_get_type                 (void) G_GNUC_CONST;

GtkWidget           *glade_palette_new                      (const GList  *catalogs);

void                 glade_palette_deselect_current_item    (GladePalette *palette,
							     gboolean      sticky_aware);

GladeWidgetAdaptor  *glade_palette_get_current_item         (GladePalette *palette);

GladeItemAppearance  glade_palette_get_item_appearance      (GladePalette *palette);

void                 glade_palette_set_item_appearance      (GladePalette       *palette,
							     GladeItemAppearance item_appearance);
							     
gboolean             glade_palette_get_use_small_item_icons (GladePalette *palette);

void		     glade_palette_set_use_small_item_icons (GladePalette *palette,
							     gboolean      use_small_item_icons);
							     
void		     glade_palette_set_show_selector_button (GladePalette *palette,
							     gboolean      show_selector_button);
							     
gboolean             glade_palette_get_show_selector_button (GladePalette *palette);

void                 glade_palette_refresh                  (GladePalette *palette);

GladeWidget         *glade_palette_create_root_widget       (GladePalette *palette,
							     GladeWidgetAdaptor *adaptor);

G_END_DECLS

#endif /* __GLADE_PALETTE_H__ */

